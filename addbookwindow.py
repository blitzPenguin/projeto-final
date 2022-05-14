from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import conexao


# Função submissão Novo Livro
def adicionar_livro(
        entry_titulo,
        entry_autor,
        entry_editora,
        entry_publicacao,
        entry_genero,
        entry_isbn
):
    con = conexao.connect()
    cursor = conexao.create_cursor(con)
    try:
        query_statement = '''INSERT INTO LIVROS (isbn, titulo, autor, editora, data_publicacao)
            VALUES (\''''+entry_isbn.get()+'\', \''+entry_titulo.get()+'\', \''+entry_autor.get()+'\', \''+entry_editora.get()+'\', \''+entry_publicacao.get()+'\')'
        conexao.query(cursor, query_statement)
        query_statement = '''SELECT MAX(id) FROM LIVROS'''
        conexao.query(cursor, query_statement)
        id_livro = cursor.fetchone()
        print(id_livro[0])
        print(entry_genero.get())
        query_statement = '''INSERT INTO LIVROS_GENEROS (id_livro, id_genero)
            VALUES (\''''+str(id_livro[0])+'\', \''+entry_genero.get()+'\')'
        conexao.query(cursor, query_statement)
    except Exception:
        messagebox.showerror(title='Erro', message='Não foi possivel adicionar o livro à base de dados')
        con.close()
    else:
        if messagebox.askyesno(title='Confirmação', message='Tem a certeza que quer adicionar o livro à base de dados?'):
            con.commit()
            entry_isbn.delete(0, END)
            entry_titulo.delete(0, END)
            entry_autor.delete(0, END)
            entry_editora.delete(0, END)
            entry_publicacao.delete(0, END)
            entry_genero.delete(0, END)
        con.close()


# Função construtora


def criar_janela():

    # Criar janela toplevel
    add_window = Toplevel()
    add_window.title('Adicionar Livro')
    add_window.geometry(
        '400x300'
    )
    add_window.minsize(
        400,
        300
    )
    add_window.maxsize(
        400,
        300
    )

    # Frame Principal
    frame_principal = ttk.Frame(
        add_window,
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
    entry_titulo = ttk.Entry(
        frame_titulo
    )
    entry_titulo.pack(
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
    entry_autor = ttk.Entry(
        frame_autor
    )
    entry_autor.pack(
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
    entry_editora = ttk.Entry(
        frame_editora
    )
    entry_editora.pack(
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
        text='Data Publicação: '
    )
    label_publicacao.pack(
        side=LEFT
    )
    entry_publicacao = ttk.Entry(
        frame_publicacao
    )
    entry_publicacao.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Introdução de Genre
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
    entry_genero = ttk.Entry(
        frame_genero
    )
    entry_genero.pack(
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
    entry_isbn = ttk.Entry(
        frame_isbn
    )
    entry_isbn.pack(
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
    botao_add = ttk.Button(
        frame_botoes,
        text='Adicionar Livro',
        command=lambda: adicionar_livro(
            entry_titulo,
            entry_autor,
            entry_editora,
            entry_publicacao,
            entry_genero,
            entry_isbn
        )
    )
    botao_cancel = ttk.Button(
        frame_botoes,
        text='Cancelar',
        command=lambda: add_window.destroy()
    )
    botao_add.grid(
        row=0,
        column=0
    )
    botao_cancel.grid(
        row=0,
        column=1
    )
    add_window.mainloop()

