# mainwindow.py #
# Função referente à criação da janela principal #


from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk
import addbookwindow
import funcoes
import removewindow


# Função construtora


def criar_janela():

    # Janela
    janela = themed_tk.ThemedTk(
        theme='breeze'
    )
    janela.title('Biblioteca Escolar')
    janela.minsize(
        1024,
        768
    )
    if janela.winfo_screenheight() >= 900:
        janela.geometry(
            '1200x900'
        )
    else:
        janela.geometry(
            '1024x768'
        )
    janela.resizable(
        width=TRUE,
        height=TRUE
    )

    # Barra Topo
    barra_menu = Menu(janela)
    janela.config(menu=barra_menu)
    menu_ficheiro = Menu(
        barra_menu,
        tearoff=0,
    )
    menu_editar = Menu(
        barra_menu,
        tearoff=0,
    )
    barra_menu.add_cascade(
        label='Ficheiro',
        menu=menu_ficheiro,
    )
    menu_ficheiro.add_command(
        label='Acrescentar Livro',
        command=lambda: addbookwindow.criar_janela()
    )
    menu_ficheiro.add_command(
        label='Remover Livro',
        command=lambda: removewindow.criar_janela()
    )
    menu_ficheiro.add_command(
        label='Sair',
        command=quit,
    )
    barra_menu.add_cascade(
        label='Editar',
        menu=menu_editar,
    )
    menu_editar.add_command(
        label='Copiar',
        command=lambda: funcoes.copiar(janela, entrada_pesquisa)
    )
    menu_editar.add_command(
        label='Cortar',
        command=lambda: funcoes.cortar(janela, entrada_pesquisa)
    )
    menu_editar.add_command(
        label='Colar',
        command=lambda: funcoes.colar(janela, entrada_pesquisa)
    )

    # Menu Botão Lado Direito Rato
    menu_lado_direito = Menu(
        janela,
        tearoff=0
    )
    menu_lado_direito.add_command(
        label="Copiar",
        command=lambda: funcoes.copiar(janela, entrada_pesquisa)
    )
    menu_lado_direito.add_command(
        label="Cortar",
        command=lambda: funcoes.cortar(janela, entrada_pesquisa)
    )
    menu_lado_direito.add_command(
        label="Colar",
        command=lambda: funcoes.colar(janela, entrada_pesquisa)
    )

    def botao_direito(event):
        try:
            menu_lado_direito.tk_popup(event.x_root, event.y_root)
        finally:
            menu_lado_direito.grab_release()

    # Frame Principal
    frame_principal = ttk.Frame(
        janela,
        padding=5
    )
    frame_principal.pack(
        fill=BOTH,
        expand=TRUE,
        anchor=CENTER
    )

    # Frame Logotipo
    frame_logotipo = ttk.Frame(
        frame_principal,
    )
    frame_logotipo.pack(
        side=TOP,
        expand=TRUE,
        fill=BOTH,
        anchor=CENTER
    )

    # Label logótipo
    logotipo = PhotoImage(
        file='./imagens/logo4.png'
    )
    label_logotipo = ttk.Label(
        frame_logotipo,
        image=logotipo,
        anchor=CENTER
    )
    label_logotipo.pack(
        side=TOP,
        expand=TRUE,
        fill=BOTH,
    )

    # Frame Lista Entregas Pendentes / Atrasadas
    frame_pendentes = ttk.Frame(
        frame_principal,
    )
    frame_pendentes.pack(
        expand=TRUE,
        fill=BOTH,
        anchor=CENTER
    )
    for i in range(2):
        frame_pendentes.grid_columnconfigure(
            i,
            weight=1
        )

    # Lista Entregas Pendentes
    label_pendentes = ttk.Label(
        frame_pendentes,
        text='Entregas pendentes:'
    )
    label_pendentes.grid(
        row=0,
        column=0,
        sticky=N
    )
    colunas = ('Aluno', 'Turma', 'Titulo do Livro', 'Data Limite')
    lista_pendentes = ttk.Treeview(
        frame_pendentes,
        columns=colunas,
        show='headings',
        height=5,
        selectmode=EXTENDED
    )
    for i in colunas:
        lista_pendentes.heading(i, text=i)
        lista_pendentes.column(i, width=10, anchor=CENTER)
    lista_pendentes.grid(
        row=1,
        column=0,
        sticky=NSEW
    )
    funcoes.requisicoes_pendentes(lista_pendentes)

    # Lista Entregas Atrasadas
    label_atrasadas = ttk.Label(
        frame_pendentes,
        text='Entregas em atraso:'
    )
    label_atrasadas.grid(
        row=0,
        column=1,
        sticky=N
    )
    lista_atrasadas = ttk.Treeview(
        frame_pendentes,
        columns=colunas,
        show='headings',
        height=5,
        selectmode=EXTENDED
    )
    for i in colunas:
        lista_atrasadas.heading(i, text=i)
        lista_atrasadas.column(i, width=10, anchor=CENTER)
    lista_atrasadas.grid(
        row=1,
        column=1,
        sticky=NSEW
    )
    funcoes.requisicoes_atrasadas(lista_atrasadas)

    # Frame de  Entrada de Procuras
    frame_pesquisa = ttk.Frame(
        frame_principal,
    )
    frame_pesquisa.pack(
        fill=BOTH,
        expand=TRUE,
        anchor=CENTER
    )

    # Entrada de Procuras
    label_pesquisa = ttk.Label(
        frame_pesquisa,
        text='Pesquisa de livros'
    )
    label_pesquisa.pack(
        side=TOP,
        anchor=N
    )
    entrada_pesquisa = ttk.Entry(
        frame_pesquisa,
    )
    botao_pesquisa = ttk.Button(
        frame_pesquisa,
        text='Pesquisar Livro',
        command=lambda: funcoes.procurar_livro(entrada_pesquisa, lista_pesquisa),
        padding=5
    )
    entrada_pesquisa.pack(
        side=LEFT,
        anchor=NW,
        fill=X,
        expand=TRUE,
    )
    entrada_pesquisa.bind("<Button-3>", botao_direito)
    botao_pesquisa.pack(
        side=LEFT,
        anchor=NE,
        expand=FALSE,
    )

    # Frame Lista de Procuras
    frame_pesquisa_lista = ttk.Frame(
        frame_principal,
    )
    frame_pesquisa_lista.pack(
        fill=BOTH,
        expand=TRUE,
        anchor=CENTER
    )

    # Lista de Procuras
    colunas = ('Titulo', 'Autor', 'Editora', 'Publicação', 'Género', 'ISBN', 'Requisitado')
    lista_pesquisa = ttk.Treeview(
        frame_pesquisa_lista,
        columns=colunas,
        show='headings',
        height=5,
        selectmode=EXTENDED,
    )
    for i in colunas:
        lista_pesquisa.heading(i, text=i)
        lista_pesquisa.column(i, width=10, anchor='center')
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
        fill=BOTH,
        expand=TRUE
    )
    for i in range(2):
        frame_botoes.grid_columnconfigure(
            i,
            weight=1
        )

    # Botões
    botao_add = ttk.Button(
        frame_botoes,
        text='Adicionar Requisição',
        command=lambda: funcoes.requisitar_livro_dialog(lista_pesquisa, lista_pendentes)
    )
    botao_deliver = ttk.Button(
        frame_botoes,
        text='Entregar Livro',
        command=lambda: funcoes.entregar_livro(lista_pendentes, lista_atrasadas)
    )
    botao_add.grid(
        row=0,
        column=0,
    )
    botao_deliver.grid(
        row=0,
        column=1,
    )
    janela.mainloop()
