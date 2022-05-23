'''
requisicaodialog.py
Função referente à construção da janela que regista as requisições de livros
'''

import tkinter as tk
from tkinter import ttk
import time
import funcoes


def criar_dialog(
    id_livro,
    titulo_livro,
    list_pending
):
    '''Criação da janela de requisições'''
    janela_dialogo = tk.Toplevel()
    janela_dialogo.title(
        "Janela Requisição"
    )
    janela_dialogo.geometry(
        "400x300"
    )
    janela_dialogo.minsize(
        400,
        300
    )
    janela_dialogo.maxsize(
        400,
        300
    )

    frame_principal = ttk.Frame(
        janela_dialogo,
        padding=5
    )
    frame_principal.pack(
        expand=tk.TRUE,
        fill=tk.BOTH
    )

    frame_titulo = ttk.Frame(
        frame_principal
    )
    frame_titulo.pack(
        expand=tk.TRUE,
        fill=tk.BOTH
    )

    label_titulo = ttk.Label(
        frame_titulo,
        text="Título: "
    )
    label_titulo.pack(
        side=tk.LEFT
    )
    display_titulo = ttk.Label(
        frame_titulo,
        text=titulo_livro
    )
    display_titulo.pack(
        side=tk.RIGHT,
        expand=tk.TRUE,
        fill=tk.X
    )

    frame_id_aluno = ttk.Frame(
        frame_principal
    )
    frame_id_aluno.pack(
        expand=tk.TRUE,
        fill=tk.BOTH
    )

    lable_id_aluno = ttk.Label(
        frame_id_aluno,
        text="ID Aluno: "
    )
    lable_id_aluno.pack(
        side=tk.LEFT
    )
    entrada_id_aluno = ttk.Combobox(
        frame_id_aluno
    )
    entrada_id_aluno['values'] = funcoes.lista_alunos()
    entrada_id_aluno.pack(
        side=tk.RIGHT,
        expand=tk.TRUE,
        fill=tk.X
    )

    frame_data_requisicao = ttk.Frame(
        frame_principal
    )
    frame_data_requisicao.pack(
        expand=tk.TRUE,
        fill=tk.BOTH
    )

    label_data_requisicao = ttk.Label(
        frame_data_requisicao,
        text="Data Requisição: "
    )
    label_data_requisicao.pack(
        side=tk.LEFT
    )
    current_time = time.strftime(
        "%d %b %Y", time.localtime()
    )
    display_data_requisicao = ttk.Label(
        frame_data_requisicao, text=current_time
    )
    display_data_requisicao.pack(
        side=tk.RIGHT,
        expand=tk.TRUE,
        fill=tk.X
    )

    frame_data_limite = ttk.Frame(
        frame_principal
    )
    frame_data_limite.pack(
        expand=tk.TRUE,
        fill=tk.BOTH
    )

    label_data_limite = ttk.Label(
        frame_data_limite,
        text="Data de Entrega: "
    )
    label_data_limite.pack(
        side=tk.LEFT
    )
    limit_time = time.strftime(
        "%d %b %Y",
        time.strptime(time.ctime(time.time() + 604800))
    )
    display_data_limite = ttk.Label(
        frame_data_limite,
        text=limit_time
    )
    display_data_limite.pack(
        side=tk.RIGHT,
        expand=tk.TRUE,
        fill=tk.X
    )

    frame_botoes = ttk.Frame(
        frame_principal,
    )
    frame_botoes.pack(anchor=tk.CENTER, side=tk.BOTTOM, fill=tk.X)
    for j in range(2):
        frame_botoes.grid_columnconfigure(
            j,
            weight=1
        )

    botao_aceitar = ttk.Button(
        frame_botoes,
        text="Adicionar Livro",
        command=lambda: funcoes.adicionar_requisicao(
            janela_dialogo,
            id_livro,
            entrada_id_aluno,
            list_pending
        ),
    )
    botao_cancelar = ttk.Button(
        frame_botoes, text="Cancelar", command=janela_dialogo.destroy
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
