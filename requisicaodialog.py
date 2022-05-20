# requisicaodialog.py #
# Função referente à construção da janela que regista as requisições de livros #


from tkinter import *
from tkinter import ttk
import time
import funcoes


# Função criadora de janela


def criar_dialog(id_livro, titulo_livro, list_pending):
    janela_dialogo = Toplevel()
    janela_dialogo.title(
        'Janela Requisição'
    )
    janela_dialogo.geometry(
        '400x300'
    )
    janela_dialogo.minsize(
        400,
        300
    )
    janela_dialogo.maxsize(
        400,
        300
    )

    # Frame Principal
    frame_principal = ttk.Frame(
        janela_dialogo,
        padding=5
    )
    frame_principal.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Frame Titulo
    frame_titulo = ttk.Frame(
        frame_principal
    )
    frame_titulo.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Display Título
    label_titulo = ttk.Label(
        frame_titulo,
        text='Título: '
    )
    label_titulo.pack(
        side=LEFT
    )
    display_titulo = ttk.Label(
        frame_titulo,
        text=titulo_livro
    )
    display_titulo.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Indtrodução ID aluno
    frame_id_aluno = ttk.Frame(
        frame_principal
    )
    frame_id_aluno.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Introdução ID aluno
    lable_id_aluno = ttk.Label(
        frame_id_aluno,
        text='ID Aluno: '
    )
    lable_id_aluno.pack(
        side=LEFT
    )
    entrada_id_aluno = ttk.Entry(
        frame_id_aluno
    )
    entrada_id_aluno.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Data Requisição
    frame_data_requisicao = ttk.Frame(
        frame_principal
    )
    frame_data_requisicao.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Display Data Requisição
    label_data_requisicao = ttk.Label(
        frame_data_requisicao,
        text='Data Requisição: '
    )
    label_data_requisicao.pack(
        side=LEFT
    )
    current_time = time.strftime("%d %b %Y", time.localtime())
    display_data_requisicao = ttk.Label(
        frame_data_requisicao,
        text=current_time
    )
    display_data_requisicao.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Data Limite
    frame_data_limite = ttk.Frame(
        frame_principal
    )
    frame_data_limite.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Display Data Limite
    label_data_limite = ttk.Label(
        frame_data_limite,
        text='Data de Entrega: '
    )
    label_data_limite.pack(
        side=LEFT
    )
    limit_time = time.strftime("%d %b %Y", time.strptime(time.ctime(time.time() + 604800)))
    display_data_limite = ttk.Label(
        frame_data_limite,
        text=limit_time
    )
    display_data_limite.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Botões
    frame_botoes = ttk.Frame(
        frame_principal,
    )
    frame_botoes.pack(
        anchor=CENTER,
        side=BOTTOM,
        fill=X
    )
    for j in range(2):
        frame_botoes.grid_columnconfigure(
            j,
            weight=1
        )

    # Botões Submeter Cancelar
    botao_aceitar = ttk.Button(
        frame_botoes,
        text='Adicionar Livro',
        command=lambda: funcoes.adicionar_requisicao(
            janela_dialogo,
            id_livro,
            entrada_id_aluno,
            list_pending
        )
    )
    botao_cancelar = ttk.Button(
        frame_botoes,
        text='Cancelar',
        command=janela_dialogo.destroy
    )
    botao_aceitar.grid(
        row=0,
        column=0
    )
    botao_cancelar.grid(
        row=0,
        column=1
    )

    janela_dialogo.mainloop()