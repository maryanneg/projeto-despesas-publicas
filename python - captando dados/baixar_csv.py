import customtkinter as ctk
import requests
import os
import zipfile
from tkinter import messagebox
import threading

DIRETORIO_DESTINO = "dados_despesa"

MESES = {
    "JANEIRO": "01", "FEVEREIRO": "02", "MARÇO": "03",
    "ABRIL": "04", "MAIO": "05", "JUNHO": "06",
    "JULHO": "07", "AGOSTO": "08", "SETEMBRO": "09",
    "OUTUBRO": "10", "NOVEMBRO": "11", "DEZEMBRO": "12"
}

def baixar_e_extrair_thread():
    ano = combo_ano.get()
    mes_nome = combo_mes.get().upper()

    if not ano or not mes_nome:
        messagebox.showwarning("Aviso", "Por favor, selecione o ano e o mês.")
        return

    if ano == "Todos":
        anos = [str(a) for a in range(2014, 2026)]
    else:
        anos = [ano]

    if mes_nome == "TODOS":
        meses = list(MESES.values())
    else:
        mes_num = MESES.get(mes_nome)
        meses = [mes_num]

    total = len(anos) * len(meses)
    count = 0

    erros = []
    baixados = []

    os.makedirs(DIRETORIO_DESTINO, exist_ok=True)

    for a in anos:
        for m in meses:
            count += 1

            status_text = f"Baixando {count} de {total} ({a}/{m})"
            janela.after(0, atualizar_status, status_text)

            codigo = f"{a}{m}"
            url = f"https://portaldatransparencia.gov.br/download-de-dados/despesas-execucao/{codigo}"
            nome_zip = f"despesas-execucao-{codigo}.zip"
            caminho_zip = os.path.join(DIRETORIO_DESTINO, nome_zip)

            try:
                resposta = requests.get(url)
                resposta.raise_for_status()

                with open(caminho_zip, "wb") as f:
                    f.write(resposta.content)

                with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                    zip_ref.extractall(DIRETORIO_DESTINO)

                os.remove(caminho_zip)

                baixados.append(codigo)

            except requests.exceptions.RequestException:
                erros.append(codigo)
            except zipfile.BadZipFile:
                erros.append(codigo)


    def fim():
        mensagem = ""
        if baixados:
            mensagem += f"Downloads concluídos para: {', '.join(baixados)}\n"
        if erros:
            mensagem += f"Falha ao baixar/extrair: {', '.join(erros)}"
        if mensagem:
            messagebox.showinfo("Resultado", mensagem)
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo baixado.")
        atualizar_status("Pronto!")

    janela.after(0, fim)

def atualizar_status(texto):
    label_status.configure(text=texto)

def iniciar_download():

    thread = threading.Thread(target=baixar_e_extrair_thread)
    thread.start()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("650x500")
janela.title("Despesas")

titulo = ctk.CTkLabel(janela, text="Despesas Públicas", font=ctk.CTkFont(family="Tahoma", size=30, weight="bold"))
titulo.pack(pady=(13,2))
legenda = ctk.CTkLabel(janela, text="Selecione os filtros disponíveis e clique em Baixar", font=ctk.CTkFont(size=10))
legenda.pack(pady=(0, 10))

frame = ctk.CTkFrame(janela, corner_radius=10)
frame.pack(pady=10, padx=20, fill="both", expand=True)

label_ano = ctk.CTkLabel(frame, text="Ano:")
label_ano.pack(pady=(20, 5))
valores_ano = ["Todos"] + [str(a) for a in range(2014, 2026)]
combo_ano = ctk.CTkComboBox(frame, values=valores_ano)
combo_ano.pack()

label_mes = ctk.CTkLabel(frame, text="Mês:")
label_mes.pack(pady=(20, 5))
valores_mes = ["Todos"] + list(MESES.keys())
combo_mes = ctk.CTkComboBox(frame, values=valores_mes)
combo_mes.pack()

botao = ctk.CTkButton(frame, text="Baixar e Extrair", command=iniciar_download,
                      font=ctk.CTkFont(family="Tahoma", size=13, weight="bold"),
                      width=200, height=40)
botao.pack(pady=(30))

label_status = ctk.CTkLabel(janela, text="")
label_status.pack(pady=(5, 20))

janela.mainloop()
