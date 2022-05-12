from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import conexao


# Funções

def remover_livro():
    pass


# Função Construtora


def criar_janela():

    # Criar janela toplevel
    remove_window = Toplevel()
    remove_window.geometry(
        '400x300'
    )
    remove_window.minsize(
        400,
        300
    )
    remove_window.maxsize(
        400,
        300
    )

    # Frame Principal
    frame_principal = ttk.Frame(
        remove_window,
        padding=5
    )
    frame_principal.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Frame de  Entrada de Procuras
    frame_search = ttk.Frame(
        frame_principal,
    )
    frame_search.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Entrada de Procuras
    entry_search = ttk.Entry(
        frame_search
    )
    button_search = ttk.Button(
        frame_search,
        text='Pesquisar Livro'
    )
    entry_search.pack(
        side=LEFT,
        anchor=NW,
        fill=X,
        expand=TRUE,
        pady=3
    )
    button_search.pack(
        side=LEFT,
        anchor=NE,
        expand=FALSE,
    )

    # Frame Lista de Procuras
    frame_search_list = ttk.Frame(
        frame_principal,
    )
    frame_search_list.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Lista de Procuras
    list_search = Listbox(
        frame_search_list
    )
    list_search.pack(
        fill=X
    )

    # Frame Botões
    frame_botoes = ttk.Frame(
        frame_principal,
    )
    frame_botoes.pack(
        anchor=CENTER,
        side=BOTTOM,
        fill=X,
        expand=TRUE
    )
    for j in range(2):
        frame_botoes.grid_columnconfigure(
            j,
            weight=1
        )

    # Botões
    botao_remove = ttk.Button(
        frame_botoes,
        text='Remover Livro',
        command=lambda: remover_livro()
    )
    botao_remove.grid(
        row=0,
        column=0
    )
    botao_cancel = ttk.Button(
        frame_botoes,
        text='Cancelar',
        command=lambda: remove_window.destroy()
    )
    botao_cancel.grid(
        row=0,
        column=1
    )
    remove_window.mainloop()
