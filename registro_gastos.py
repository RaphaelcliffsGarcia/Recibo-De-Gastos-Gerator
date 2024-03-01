from fpdf import FPDF
from datetime import date
from tkinter import *
from tkinter.messagebox import showinfo 


def criar_recibo():
    def gerar_recibo():
        # Obtendo informações do usuário
        vlr = entrada_valor.get()
        descricao = entrada_descricao.get()
        categoria = entrada_categoria.get()
        metodo_pagamento = entrada_metodo_pagamento.get()

        # Convertendo o valor para reais
        vlr_msg = f"{vlr} reais"

        # Obtendo a data atual
        data = date.today()
        dia = data.day
        mes = data.month
        ano = data.year

        # Criando o recibo em PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 20)
        width = pdf.w
        height = pdf.h
        pdf.image("dados/rec.jpg", x=0, y=0, w=width, h=height)
        pdf.set_text_color(255, 0, 0)
        pdf.text(162, 49, vlr_msg)
        pdf.set_text_color(0, 0, 0)
        pdf.text(80, 91, descricao)
        pdf.text(80, 116, categoria)
        pdf.text(80, 141, metodo_pagamento)
        pdf.text(30, 197, str(dia))
        pdf.text(50, 197, str(mes))
        pdf.text(70, 197, str(ano))
        name_archive = f"{descricao.strip()}_{dia}_{mes}_{ano}"
        pdf.output(f'{name_archive}.pdf')

        # Exibindo mensagem de sucesso
        showinfo("Sucesso", "Recibo gerado com sucesso!")

    # Configuração da janela tkinter
    janela = Tk()
    janela.title('Register Pro')
    janela.geometry("400x350")  # Definindo o tamanho da janela
    

    # Configuração do frame para organização dos elementos
    frame = Frame(janela)
    frame.pack(pady=10)  # Adicionando padding apenas na vertical para centralizar

    # Entradas de texto para as informações do recibo
    Label(frame, text="Valor do Gasto:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entrada_valor = Entry(frame)
    entrada_valor.grid(row=0, column=1, padx=10, pady=5)

    Label(frame, text="Tipo do Gasto:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entrada_descricao = Entry(frame)
    entrada_descricao.grid(row=1, column=1, padx=10, pady=5)

    Label(frame, text="Categoria do Gasto:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entrada_categoria = Entry(frame)
    entrada_categoria.grid(row=2, column=1, padx=10, pady=5)

    Label(frame, text="Método do Pagamento:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    entrada_metodo_pagamento = Entry(frame)
    entrada_metodo_pagamento.grid(row=3, column=1, padx=10, pady=5)

    # Botão para gerar o recibo
    botao_gerar_recibo = Button(janela, text="Gerar Recibo", command=gerar_recibo)
    botao_gerar_recibo.pack(pady=10)  # Adicionando padding apenas na vertical para centralizar
     # Adicionando a logo
    logo = PhotoImage(file="dados/logo.png")
    logo_label = Label(janela, image=logo)
    logo_label.image = logo  # Para evitar garbage collection
    logo_label.pack(pady=5)

    janela.mainloop()

criar_recibo()
