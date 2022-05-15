# removewindow.py #
# Função referente à criação da janela de desativação de livros na base de dados #


from tkinter import *
from tkinter import ttk
import funcoes


# Função Construtora


def criar_janela():

    # Criar janela toplevel
    remove_window = Toplevel()
    remove_window.geometry(
        '600x400'
    )
    remove_window.minsize(
        600,
        400
    )
    remove_window.maxsize(
        600,
        400
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
        text='Pesquisar Livro',
        command=lambda: funcoes.procurar_livro(entry_search, list_search)
    )
    entry_search.pack(
        side=LEFT,
        anchor=NW,
        fill=X,
        expand=TRUE,
    )
    button_search.pack(
        side=LEFT,
        anchor=NE,
        expand=FALSE,
        pady=1
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
    colunas = ('Titulo', 'Autor', 'Editora', 'Publicação', 'Género', 'ISBN')
    list_search = ttk.Treeview(
        frame_search_list,
        columns=colunas,
        show='headings',
        selectmode=EXTENDED,
    )
    for i in colunas:
        list_search.heading(i, text=i)
        list_search.column(i, width=10, anchor='center')
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
        command=lambda: funcoes.remover_livro(
            remove_window,
            list_search
        )
    )
    botao_remove.grid(
        row=0,
        column=0
    )
    botao_cancel = ttk.Button(
        frame_botoes,
        text='Cancelar',
        command=remove_window.destroy
    )
    botao_cancel.grid(
        row=0,
        column=1
    )
    remove_window.mainloop()
