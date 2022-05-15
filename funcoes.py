# funcoes.py #
# Funções referentes ao funcionamento do programa #

import conexao
import requisicaodialog
from tkinter import *
from tkinter import messagebox


# Funções de copiar, cortar e colar


def copiar(
        janela,
        entrada
):
    janela.clipboard_clear()
    janela.clipboard_append(
        entrada.selection_get()
    )


def cortar(
        janela,
        entrada
):
    janela.clipboard_clear()
    janela.clipboard_append(
        entrada.selection_get()
    )
    if entrada.index(ANCHOR) < entrada.index(INSERT):
        entrada.delete(
            ANCHOR,
            INSERT
        )
    elif entrada.index(INSERT) < entrada.index(ANCHOR):
        entrada.delete(
            INSERT,
            ANCHOR
        )


def colar(
        janela,
        entrada
):
    entrada.insert(
        entrada.index(INSERT),
        janela.clipboard_get()
    )
    janela.clipboard_clear()


# Função que insere requisições pendentes na lista apropriada


def requisicoes_pendentes(
        lista
):
    con = conexao.connect()
    cursor = conexao.cursor(
        con
    )
    conexao.query_req_pendentes(
        cursor
    )
    fetch = cursor.fetchall()
    for i in lista.get_children():
        lista.delete(
            i
        )
    for i in fetch:
        lista.insert(
            '',
            END,
            values=i)
    con.close()


# Função que insere requisições atrasadas na lista apropriada


def requisicoes_atrasadas(
        lista
):
    con = conexao.connect()
    cursor = conexao.cursor(
        con
    )
    conexao.query_req_atrasadas(
        cursor
    )
    fetch = cursor.fetchall()
    for i in lista.get_children():
        lista.delete(
            i
        )
    for i in fetch:
        lista.insert(
            '',
            END,
            values=i
        )
    con.close()


# Função de pesquisa de livros


def procurar_livro(
        entrada,
        list
):
    con = conexao.connect()
    cursor = conexao.cursor(
        con
    )
    conexao.query_pesquisa(
        cursor,
        entrada
    )
    fetch = cursor.fetchall()
    for i in list.get_children():
        list.delete(
            i
        )
    for i in fetch:
        list.insert(
            '',
            END,
            values=i
        )
    con.close()


# Função de seleção de livros


def selecao_livros(
        lista,
        valor
):
    resultado = []
    for i in range(len(lista.selection())):
        resultado.append(lista.item(lista.selection()[i])['values'][valor])
    return resultado


# Funções para abertura de janela de requisição


def requisitar_livro_dialog(
        lista_pesquisa,
        lista_pendente
):
    if len(lista_pesquisa.selection()) != 0:
        livro = selecao_livros(
            lista_pesquisa,
            7
        )
        titulo = selecao_livros(
            lista_pesquisa,
            0
        )
        requisicaodialog.criar_dialog(
            livro,
            titulo,
            lista_pendente
        )


# Função para criação de requisições


def adicionar_requisicao(
        janela,
        livro,
        entrada,
        lista
):
    try:
        aluno = entrada.get()
    except Exception as e:
        print(e)
        messagebox.showerror(
            'Erro',
            'Introdução de  id do aluno inválida'
        )
    else:
        try:
            con = conexao.connect()
        except Exception as e:
            print(e)
            messagebox.showerror(
                'Erro',
                'Erro de conexão à base de dados'
            )
            janela.destroy()
        else:
            cursor = conexao.cursor(
                con
            )
            conexao.query_requisicao_cabecalho(
                cursor,
                aluno
            )
            if messagebox.askyesno('Confirmação', 'Deseja confirmar a requisição?'):
                for i in livro:
                    conexao.query_requisicao_descricao(
                        cursor,
                        i
                    )
                try:
                    con.commit()
                except Exception as e:
                    print(e)
                    messagebox.showerror(
                        'Erro',
                        'Erro de conexão à base de dados.\nNão foi possível concluir a requisição.'
                    )
                    con.close()
                else:
                    messagebox.showinfo(
                        'Sucesso',
                        'Requisição concluida com sucesso.'
                    )
                    con.close()
                    requisicoes_pendentes(
                        lista
                    )
                    janela.destroy()


# Função para entrega de livros


def entrega_livro(
        lista,
        *args
):
    livro = selecao_livros(
        lista,
        4
    )
    titulo = selecao_livros(
        lista,
        1
    )
    if messagebox.askyesno('Confirmação', 'Deseja entregas o(s) seguinte(s) livro(s): ' + str(titulo)):
        try:
            con = conexao.connect()
            cursor = conexao.cursor(
                con
            )
        except Exception as e:
            print(e)
            messagebox.showerror(
                'Erro',
                'Erro de conexão à base de dados.'
            )
        else:
            for i in livro:
                conexao.query_entregar_livro(
                    cursor,
                    i
                )
            # multa = 1
            # if any(vars(args).values()):
                # messagebox.showwarning(
                # 'Multa',
                # 'Pagamento de multa: '+str(multa)+' €'
                # )
            try:
                con.commit()
            except Exception as e:
                print(e)
                messagebox.showerror(
                    'Erro',
                    'Erro de conexão à base de dados. Não foi possível concluir a entrega.'
                )
                con.close()
            else:
                con.close()
                if len(livro) == 1:
                    messagebox.showinfo(
                        'Sucesso',
                        'O livro ' + str(titulo) + ' foi entregue com sucesso.'
                    )
                elif len(livro) > 1:
                    messagebox.showinfo(
                        'Sucesso',
                        'Os livros ' + str(titulo) + ' foram entregues com sucesso.'
                    )


# Função para iniciar processo de entrega de livros


def entregar_livro(
        lista_pendente,
        lista_atrasadas
):
    if len(lista_pendente.selection()) != 0:
        entrega_livro(
            lista_pendente
        )
        requisicoes_pendentes(
            lista_pendente
        )
    if len(lista_atrasadas.selection()) != 0:
        entrega_livro(
            lista_atrasadas,
            1
        )
        requisicoes_atrasadas(
            lista_atrasadas
        )


# Função para adição de livros


def adicionar_livro(
        janela,
        titulo,
        autor,
        editora,
        publicacao,
        genero,
        isbn
):
    try:
        con = conexao.connect()
    except Exception as e:
        print(e)
        messagebox.showerror(
            'Erro',
            'Erro de conexão à base de dados.'
        )
    else:
        cursor = conexao.cursor(
            con
        )
        try:
            conexao.query_adicionar_livro(
                cursor,
                titulo,
                autor,
                editora,
                publicacao,
                isbn
            )
        except Exception as e:
            print(e)
            con.close()
        try:
            conexao.query_adicionar_genero(
                cursor,
                genero
            )
        except Exception as e:
            print(e)
            con.close()
        else:
            if messagebox.askyesno('Confirmação', 'Deseja adicionar o livro '+str(titulo.get())+'?'):
                try:
                    con.commit()
                except Exception as e:
                    print(e)
                    messagebox.showerror(
                        'Erro',
                        'Erro na conexão à base de dados. O livro não foi adicionado.'
                    )
                    con.close()
                else:
                    con.close()
                    lista_apagar = (titulo, autor, editora, publicacao, isbn, genero)
                    for i in lista_apagar:
                        i.delete(0, END)
                    janela.destroy()


# Função para remoção de livros


def remover_livro(
        janela,
        lista
):
    if len(lista.selection()) != 0:
        livro = selecao_livros(
            lista,
            7
        )
        titulo = selecao_livros(
            lista,
            0
        )
        if messagebox.askyesno('Confirmação', 'Deseja remover o(s) seguinte(s) livro(s)? '+str(titulo)):
            try:
                con = conexao.connect()
            except Exception as e:
                print(e)
                messagebox.showerror(
                    'Erro',
                    'Erro de conexão à base de dados.'
                )
            else:
                cursor = conexao.cursor(
                    con
                )
                for i in livro:
                    conexao.query_remover_livro(
                        cursor,
                        i
                    )
                    print(i)
                try:
                    con.commit()
                except Exception as e:
                    print(e)
                    messagebox.showerror(
                        'Erro',
                        'Erro na conexão à base de dados. Não foi possível remover o(s) livro(s).'
                    )
                    con.close()
                    janela.destroy()
                else:
                    con.close()
                    if len(livro) == 1:
                        messagebox.showinfo(
                            'Sucesso',
                            'O livro '+str(titulo)+' foi removido com sucesso.'
                        )
                    elif len(livro) > 1:
                        messagebox.showinfo(
                            'Sucesso',
                            'Os livros '+str(titulo)+' foram removidos com sucesso.'
                        )
                    janela.destroy()
