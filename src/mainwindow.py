'''
mainwindow.py
Função referente à criação da janela principal'''


import tkinter as tk
from tkinter import ttk
from ttkthemes import themed_tk
import os
import addbookwindow
import funcoes
import removewindow


def criar_janela():
    '''Construtor da janela principal'''
    janela = themed_tk.ThemedTk(
        theme='breeze'
    )
    janela.title(
        'Biblioteca Escolar'
    )
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
        width=tk.TRUE,
        height=tk.TRUE
    )

    # Barra Topo
    barra_menu = tk.Menu(
        janela
    )
    janela.config(
        menu=barra_menu
    )
    menu_ficheiro = tk.Menu(
        barra_menu,
        tearoff=0,
    )
    menu_editar = tk.Menu(
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
        command=janela.destroy,
    )
    barra_menu.add_cascade(
        label='Editar',
        menu=menu_editar,
    )
    menu_editar.add_command(
        label='Copiar',
        command=lambda: funcoes.copiar(
            janela,
            entrada_pesquisa
        )
    )
    menu_editar.add_command(
        label='Cortar',
        command=lambda: funcoes.cortar(
            janela,
            entrada_pesquisa
        )
    )
    menu_editar.add_command(
        label='Colar',
        command=lambda: funcoes.colar(
            janela,
            entrada_pesquisa
        )
    )

    # Menu Botão Lado Direito Rato
    menu_lado_direito = tk.Menu(
        janela,
        tearoff=0
    )
    menu_lado_direito.add_command(
        label="Copiar",
        command=lambda: funcoes.copiar(
            janela,
            entrada_pesquisa
        )
    )
    menu_lado_direito.add_command(
        label="Cortar",
        command=lambda: funcoes.cortar(
            janela,
            entrada_pesquisa
        )
    )
    menu_lado_direito.add_command(
        label="Colar",
        command=lambda: funcoes.colar(
            janela,
            entrada_pesquisa
        )
    )

    def botao_direito(
        event
    ):
        try:
            menu_lado_direito.tk_popup(
                event.x_root,
                event.y_root
            )
        finally:
            menu_lado_direito.grab_release()

    # Frame Principal
    frame_principal = ttk.Frame(
        janela,
        padding=5
    )
    frame_principal.pack(
        fill=tk.BOTH,
        expand=tk.TRUE,
        anchor=tk.CENTER
    )

    # Frame Logotipo
    frame_logotipo = ttk.Frame(
        frame_principal,
    )
    frame_logotipo.pack(
        side=tk.TOP,
        expand=tk.TRUE,
        fill=tk.BOTH,
        anchor=tk.CENTER
    )

    # Label logótipo
    imagepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagens', 'logotipo.png')
    logotipo = tk.PhotoImage(
        file=imagepath
    )
    label_logotipo = ttk.Label(
        frame_logotipo,
        image=logotipo,
        anchor=tk.CENTER
    )
    label_logotipo.pack(
        side=tk.TOP,
        expand=tk.TRUE,
        fill=tk.BOTH,
    )

    # Frame Lista Entregas Pendentes / Atrasadas
    frame_pendentes = ttk.Frame(
        frame_principal,
    )
    frame_pendentes.pack(
        expand=tk.TRUE,
        fill=tk.BOTH,
        anchor=tk.CENTER
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
        sticky=tk.N
    )
    colunas = (
        'Aluno',
        'Turma',
        'Titulo do Livro',
        'Data Limite'
    )
    lista_pendentes = ttk.Treeview(
        frame_pendentes,
        columns=colunas,
        show='headings',
        height=5,
        selectmode=tk.EXTENDED
    )
    for i in colunas:
        lista_pendentes.heading(
            i,
            text=i
        )
        lista_pendentes.column(
            i,
            width=10,
            anchor=tk.CENTER
        )
    lista_pendentes.grid(
        row=1,
        column=0,
        sticky=tk.NSEW
    )
    funcoes.requisicoes_pendentes(
        lista_pendentes
    )

    # Lista Entregas Atrasadas
    label_atrasadas = ttk.Label(
        frame_pendentes,
        text='Entregas em atraso:'
    )
    label_atrasadas.grid(
        row=0,
        column=1,
        sticky=tk.N
    )
    lista_atrasadas = ttk.Treeview(
        frame_pendentes,
        columns=colunas,
        show='headings',
        height=5,
        selectmode=tk.EXTENDED
    )
    for i in colunas:
        lista_atrasadas.heading(
            i,
            text=i
        )
        lista_atrasadas.column(
            i,
            width=10,
            anchor=tk.CENTER
        )
    lista_atrasadas.grid(
        row=1,
        column=1,
        sticky=tk.NSEW
    )
    funcoes.requisicoes_atrasadas(
        lista_atrasadas
    )

    # Frame de  Entrada de Procuras
    frame_pesquisa = ttk.Frame(
        frame_principal,
    )
    frame_pesquisa.pack(
        fill=tk.BOTH,
        expand=tk.TRUE,
        anchor=tk.CENTER
    )

    # Entrada de Procuras
    label_pesquisa = ttk.Label(
        frame_pesquisa,
        text='Pesquisa de livros'
    )
    label_pesquisa.pack(
        side=tk.TOP,
        anchor=tk.N
    )
    entrada_pesquisa = ttk.Entry(
        frame_pesquisa,
    )
    botao_pesquisa = ttk.Button(
        frame_pesquisa,
        text='Pesquisar Livro',
        command=lambda: funcoes.procurar_livro(
            entrada_pesquisa,
            lista_pesquisa
        ),
        padding=5
    )
    entrada_pesquisa.pack(
        side=tk.LEFT,
        anchor=tk.NW,
        fill=tk.X,
        expand=tk.TRUE,
    )
    entrada_pesquisa.bind(
        "<Button-3>",
        botao_direito
    )
    botao_pesquisa.pack(
        side=tk.LEFT,
        anchor=tk.NE,
        expand=tk.FALSE,
    )

    # Frame Lista de Procuras
    frame_pesquisa_lista = ttk.Frame(
        frame_principal,
    )
    frame_pesquisa_lista.pack(
        fill=tk.BOTH,
        expand=tk.TRUE,
        anchor=tk.CENTER
    )

    # Lista de Procuras
    colunas = (
        'Titulo',
        'Autor',
        'Editora',
        'Publicação',
        'Género',
        'ISBN', 
        'Requisitado'
    )
    lista_pesquisa = ttk.Treeview(
        frame_pesquisa_lista,
        columns=colunas,
        show='headings',
        height=5,
        selectmode=tk.EXTENDED,
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
        fill=tk.X
    )

    # Frame Botões
    frame_botoes = ttk.Frame(
        frame_principal,
    )
    frame_botoes.pack(
        anchor=tk.CENTER,
        side=tk.BOTTOM,
        fill=tk.BOTH,
        expand=tk.TRUE
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
        command=lambda: funcoes.requisitar_livro_dialog(
            lista_pesquisa,
            lista_pendentes
        )
    )
    botao_deliver = ttk.Button(
        frame_botoes,
        text='Entregar Livro',
        command=lambda: funcoes.entregar_livro(
            lista_pendentes,
            lista_atrasadas
        )
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
    
if __name__ == '__main__':
    criar_janela()
