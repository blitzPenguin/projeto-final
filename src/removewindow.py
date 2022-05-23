'''
removewindow.py
Função referente à criação da janela de desativação de livros na base de dados'''


from tkinter import *
from tkinter import ttk
import funcoes


def criar_janela():
    '''Construtor da janela de remoção de livros'''
    janela_remover = Toplevel()
    janela_remover.geometry(
        '600x400'
    )
    janela_remover.minsize(
        600,
        400
    )
    janela_remover.maxsize(
        600,
        400
    )

    # Frame Principal
    frame_principal = ttk.Frame(
        janela_remover,
        padding=5
    )
    frame_principal.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Frame de  Entrada de Procuras
    frame_pesquisa = ttk.Frame(
        frame_principal,
    )
    frame_pesquisa.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Entrada de Procuras
    entrada_pesquisa = ttk.Entry(
        frame_pesquisa
    )
    button_search = ttk.Button(
        frame_pesquisa,
        text='Pesquisar Livro',
        command=lambda: funcoes.procurar_livro(
            entrada_pesquisa,
            lista_pesquisa
        )
    )
    entrada_pesquisa.pack(
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
    frame_pesquisa_lista = ttk.Frame(
        frame_principal,
    )
    frame_pesquisa_lista.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Lista de Procuras
    colunas = (
        'Titulo',
        'Autor',
        'Editora',
        'Publicação',
        'Género',
        'ISBN'
    )
    lista_pesquisa = ttk.Treeview(
        frame_pesquisa_lista,
        columns=colunas,
        show='headings',
        height=5,
        selectmode=EXTENDED,
    )
    for i in colunas:
        lista_pesquisa.heading(
            i,
            text=i
        )
        lista_pesquisa.column(
            i,
            width=10,
            anchor='center'
        )
    lista_pesquisa.pack(
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
    botao_remover = ttk.Button(
        frame_botoes,
        text='Remover Livro',
        command=lambda: funcoes.remover_livro(
            janela_remover,
            lista_pesquisa
        )
    )
    botao_remover.grid(
        row=0,
        column=0
    )
    botao_cancelar = ttk.Button(
        frame_botoes,
        text='Cancelar',
        command=janela_remover.destroy
    )
    botao_cancelar.grid(
        row=0,
        column=1
    )

    # Menu Botão Lado Direito Rato
    menu_lado_direito = Menu(
        janela_remover,
        tearoff=0
    )
    menu_lado_direito.add_command(
        label="Copiar",
        command=lambda: funcoes.copiar(
        janela_remover,
        entrada_pesquisa
    )
    )
    menu_lado_direito.add_command(
        label="Cortar",
        command=lambda: funcoes.cortar(
            janela_remover,
            entrada_pesquisa
        )
    )
    menu_lado_direito.add_command(
        label="Colar",
        command=lambda: funcoes.colar(
            janela_remover,
            entrada_pesquisa
        )
    )

    def botao_direito(event):
        try:
            menu_lado_direito.tk_popup(
                event.x_root,
                event.y_root
            )
        finally:
            menu_lado_direito.grab_release()

    entrada_pesquisa.bind(
        "<Button-3>",
        botao_direito
    )
    
    janela_remover.mainloop()
