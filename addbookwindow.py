# addbookwindow.py #
# Função referente à criação da janela de adição de livros à base de dados #


from tkinter import *
from tkcalendar import *
from tkinter import ttk
import funcoes


# Função construtora


def criar_janela():

    # Criar janela toplevel
    janela_adicionar = Toplevel()
    janela_adicionar.title('Adicionar Livro')
    janela_adicionar.geometry(
        '600x400'
    )
    janela_adicionar.minsize(
        600,
        400
    )
    janela_adicionar.maxsize(
        600,
        400
    )

    # Frame Principal
    frame_principal = ttk.Frame(
        janela_adicionar,
        padding=5
    )
    frame_principal.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Frame Introdução de Título
    frame_titulo = ttk.Frame(
        frame_principal,
    )
    frame_titulo.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Introdução de Título
    label_titulo = ttk.Label(
        frame_titulo,
        text='Título: '
    )
    label_titulo.pack(
        side=LEFT
    )
    entrada_titulo = ttk.Entry(
        frame_titulo
    )
    entrada_titulo.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Introdução de Autor
    frame_autor = ttk.Frame(
        frame_principal,
    )
    frame_autor.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Introdução de Autor
    label_autor = ttk.Label(
        frame_autor,
        text='Autor: '
    )
    label_autor.pack(
        side=LEFT
    )
    entrada_autor = ttk.Entry(
        frame_autor
    )
    entrada_autor.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Introdução de Editora
    frame_editora = ttk.Frame(
        frame_principal,
    )
    frame_editora.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Introdução de Editora
    label_editora = ttk.Label(
        frame_editora,
        text='Editora: '
    )
    label_editora.pack(
        side=LEFT
    )
    entrada_editora = ttk.Entry(
        frame_editora
    )
    entrada_editora.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Introdução de Publicação
    frame_publicacao = ttk.Frame(
        frame_principal,
    )
    frame_publicacao.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Introdução de Publicação
    label_publicacao = ttk.Label(
        frame_publicacao,
        text='Ano de Publicação: '
    )
    label_publicacao.pack(
        side=LEFT
    )   
    entrada_publicacao = ttk.Combobox(
        frame_publicacao,
    )
    entrada_publicacao['values'] = funcoes.lista_anos()
    entrada_publicacao.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Introdução de Genero
    frame_genero = ttk.Frame(
        frame_principal,
    )
    frame_genero.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Introdução de Genero
    label_genero = ttk.Label(
        frame_genero,
        text='Género: '
    )
    label_genero.pack(
        side=LEFT
    )
    entrada_genero = ttk.Combobox(
        frame_genero
    )
    entrada_genero['values'] = funcoes.lista_generos()
    entrada_genero.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame isbn
    frame_isbn = ttk.Frame(
        frame_principal,
    )
    frame_isbn.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Introdução do isbn
    label_isbn = ttk.Label(
        frame_isbn,
        text='ISBN: '
    )
    label_isbn.pack(
        side=LEFT
    )
    entrada_isbn = ttk.Entry(
        frame_isbn
    )
    entrada_isbn.pack(
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
    for i in range(2):
        frame_botoes.grid_columnconfigure(
            i,
            weight=1
        )

    # Botões Submeter Cancelar
    botao_adicionar = ttk.Button(
        frame_botoes,
        text='Adicionar Livro',
        command=lambda: funcoes.adicionar_livro(
            janela_adicionar,
            entrada_titulo,
            entrada_autor,
            entrada_editora,
            entrada_publicacao,
            entrada_genero,
            entrada_isbn
        )
    )
    botao_cancelar = ttk.Button(
        frame_botoes,
        text='Cancelar',
        command=janela_adicionar.destroy
    )
    botao_adicionar.grid(
        row=0,
        column=0
    )
    botao_cancelar.grid(
        row=0,
        column=1
    )

    # Menu Botão Lado Direito Rato
    menu_lado_direito_titulo = Menu(
        janela_adicionar,
        tearoff=0
    )
    menu_lado_direito_titulo.add_command(
        label="Copiar",
        command=lambda: funcoes.copiar(janela_adicionar, entrada_titulo)
    )
    menu_lado_direito_titulo.add_command(
        label="Cortar",
        command=lambda: funcoes.cortar(janela_adicionar, entrada_titulo)
    )
    menu_lado_direito_titulo.add_command(
        label="Colar",
        command=lambda: funcoes.colar(janela_adicionar, entrada_titulo)
    )

    def botao_direito_titulo(event):
        try:
            menu_lado_direito_titulo.tk_popup(event.x_root, event.y_root)
        finally:
            menu_lado_direito_titulo.grab_release()

    menu_lado_direito_autor = Menu(
        janela_adicionar,
        tearoff=0
    )
    menu_lado_direito_autor.add_command(
        label="Copiar",
        command=lambda: funcoes.copiar(janela_adicionar, entrada_autor)
    )
    menu_lado_direito_autor.add_command(
        label="Cortar",
        command=lambda: funcoes.cortar(janela_adicionar, entrada_autor)
    )
    menu_lado_direito_autor.add_command(
        label="Colar",
        command=lambda: funcoes.colar(janela_adicionar, entrada_autor)
    )

    def botao_direito_autor(event):
        try:
            menu_lado_direito_autor.tk_popup(event.x_root, event.y_root)
        finally:
            menu_lado_direito_autor.grab_release()

    menu_lado_direito_editora = Menu(
        janela_adicionar,
        tearoff=0
    )
    menu_lado_direito_editora.add_command(
        label="Copiar",
        command=lambda: funcoes.copiar(janela_adicionar, entrada_editora)
    )
    menu_lado_direito_editora.add_command(
        label="Cortar",
        command=lambda: funcoes.cortar(janela_adicionar, entrada_editora)
    )
    menu_lado_direito_editora.add_command(
        label="Colar",
        command=lambda: funcoes.colar(janela_adicionar, entrada_editora)
    )

    def botao_direito_editora(event):
        try:
            menu_lado_direito_editora.tk_popup(event.x_root, event.y_root)
        finally:
            menu_lado_direito_editora.grab_release()

    menu_lado_direito_publicacao = Menu(
        janela_adicionar,
        tearoff=0
    )
    menu_lado_direito_publicacao.add_command(
        label="Copiar",
        command=lambda: funcoes.copiar(janela_adicionar, entrada_publicacao)
    )
    menu_lado_direito_publicacao.add_command(
        label="Cortar",
        command=lambda: funcoes.cortar(janela_adicionar, entrada_publicacao)
    )
    menu_lado_direito_publicacao.add_command(
        label="Colar",
        command=lambda: funcoes.colar(janela_adicionar, entrada_publicacao)
    )

    def botao_direito_publicacao(event):
        try:
            menu_lado_direito_publicacao.tk_popup(event.x_root, event.y_root)
        finally:
            menu_lado_direito_publicacao.grab_release()

    menu_lado_direito_genero = Menu(
        janela_adicionar,
        tearoff=0
    )
    menu_lado_direito_genero.add_command(
        label="Copiar",
        command=lambda: funcoes.copiar(janela_adicionar, entrada_genero)
    )
    menu_lado_direito_genero.add_command(
        label="Cortar",
        command=lambda: funcoes.cortar(janela_adicionar, entrada_genero)
    )
    menu_lado_direito_genero.add_command(
        label="Colar",
        command=lambda: funcoes.colar(janela_adicionar, entrada_genero)
    )

    def botao_direito_genero(event):
        try:
            menu_lado_direito_genero.tk_popup(event.x_root, event.y_root)
        finally:
            menu_lado_direito_genero.grab_release()

    menu_lado_direito_isbn = Menu(
        janela_adicionar,
        tearoff=0
    )
    menu_lado_direito_isbn.add_command(
        label="Copiar",
        command=lambda: funcoes.copiar(janela_adicionar, entrada_isbn)
    )
    menu_lado_direito_isbn.add_command(
        label="Cortar",
        command=lambda: funcoes.cortar(janela_adicionar, entrada_isbn)
    )
    menu_lado_direito_isbn.add_command(
        label="Colar",
        command=lambda: funcoes.colar(janela_adicionar, entrada_isbn)
    )

    def botao_direito_isbn(event):
        try:
            menu_lado_direito_isbn.tk_popup(event.x_root, event.y_root)
        finally:
            menu_lado_direito_isbn.grab_release()

    entrada_titulo.bind("<Button-3>", botao_direito_titulo)
    entrada_autor.bind("<Button-3>", botao_direito_autor)
    entrada_editora.bind("<Button-3>", botao_direito_editora)
    entrada_publicacao.bind("<Button-3>", botao_direito_publicacao)
    entrada_genero.bind("<Button-3>", botao_direito_genero)
    entrada_isbn.bind("<Button-3>", botao_direito_isbn)
    janela_adicionar.mainloop()
