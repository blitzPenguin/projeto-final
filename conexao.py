# conexao.py #
# Funções e querys para conexão e operações entre o programa e a base de dados #

import mysql.connector


# Conexão à base de dados #


def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Biblioteca_bd"
    )


def cursor(
        con
):
    return con.cursor()


# Execucao querys #


def query_req_pendentes(
        cursor
):
    cursor.execute(
        '''
        SELECT ALUNOS.nome, titulo, data_req, data_limite, LIVROS.id
        FROM ALUNOS, LIVROS, REQUISICOES_HEADER, REQUISICOES_DESC
        WHERE
        ALUNOS.id = REQUISICOES_HEADER.id_aluno
        AND
        LIVROS.id = REQUISICOES_DESC.id_livro
        AND
        REQUISICOES_HEADER.id = REQUISICOES_DESC.id_requisicao
        AND
        REQUISICOES_DESC.devolvido = 0
        AND
        REQUISICOES_HEADER.data_limite >= DATE(NOW())
        '''
    )


def query_req_atrasadas(
        cursor
):
    cursor.execute(
        '''
        SELECT ALUNOS.nome, titulo, data_req, data_limite, LIVROS.id
        FROM ALUNOS, LIVROS, REQUISICOES_HEADER, REQUISICOES_DESC
        WHERE
        ALUNOS.id = REQUISICOES_HEADER.id_aluno
        AND
        LIVROS.id = REQUISICOES_DESC.id_livro
        AND
        REQUISICOES_HEADER.id = REQUISICOES_DESC.id_requisicao
        AND
        REQUISICOES_DESC.devolvido = 0
        AND
        REQUISICOES_HEADER.data_limite < DATE(NOW())
        '''
    )


def query_pesquisa(
        cursor,
        entrada
):
    cursor.execute(
        '''
        SELECT DISTINCT titulo,autor,editora,data_publicacao,GENEROS.designacao,isbn,REQUISITADO.designacao,LIVROS.id
        FROM LIVROS, GENEROS, LIVROS_GENEROS, REQUISITADO
        WHERE LIVROS_GENEROS.id_livro = LIVROS.id
        AND
        GENEROS.id = LIVROS_GENEROS.id_genero
        AND
        LIVROS.id_requisitado = REQUISITADO.id
        AND
        ativo = 1
        AND
        (titulo LIKE \'%'''+entrada.get()+'''%\'
        OR autor LIKE \'%'''+entrada.get()+'''%\'
        OR editora LIKE \'%'''+entrada.get()+'''%\'
        OR data_publicacao LIKE \'%'''+entrada.get()+'''%\'
        OR GENEROS.designacao LIKE \'%'''+entrada.get()+'''%\')
        ORDER BY titulo ASC
        '''
    )


def query_adicionar_livro(
        cursor,
        titulo,
        autor,
        editora,
        publicacao,
        isbn,
):
    cursor.execute(
        '''
        INSERT INTO LIVROS (titulo, autor, editora, data_publicacao, isbn)
        VALUES (\''''+titulo.get()+'\', \''+autor.get()+'\', \''+editora.get()+'''\', \'
        '''+publicacao.get()+'\', \''+isbn.get()+'''\')
        '''
    )


def query_adicionar_genero(
        cursor,
        genero
):
    cursor.execute(
        '''
        SELECT MAX(id) FROM LIVROS
        '''
    )
    livro = cursor.fetchone()
    cursor.execute(
        '''
        INSERT INTO LIVROS_GENEROS (id_livro, id_genero)
        VALUES (\''''+str(livro[0])+'\', \''+genero.get()+'''\')
        '''
    )


def query_remover_livro(
        cursor,
        livro
):
    cursor.execute(
        '''
        UPDATE LIVROS
        SET ativo = 0
        WHERE id = \''''+str(livro)+'''\'
        '''
    )


def query_requisicao_cabecalho(
        cursor,
        aluno
):
    cursor.execute(
        '''
        INSERT INTO REQUISICOES_HEADER (id_aluno, data_limite)
        VALUES (\''''+str(aluno)+'''\', DATE_ADD(CURRENT_TIMESTAMP,INTERVAL 7 DAY))
        '''
    )


def query_requisicao_descricao(
        cursor,
        livro
):
    cursor.execute(
        '''
        SELECT MAX(id) FROM REQUISICOES_HEADER
        '''
    )
    requisicao = cursor.fetchone()
    cursor.execute(
        '''
        INSERT INTO REQUISICOES_DESC (id_requisicao, id_livro)
        VALUES (\''''+str(requisicao[0])+'\', \''+str(livro)+'''\')
        '''
    )
    cursor.execute(
        '''
        UPDATE LIVROS
        SET id_requisitado = 2
        WHERE id = \''''+str(livro)+'''\'
        '''
    )


def query_entregar_livro(
        cursor,
        livro
):
    cursor.execute(
        '''
        UPDATE REQUISICOES_DESC, LIVROS
        SET REQUISICOES_DESC.devolvido = 1,
        LIVROS.id_requisitado = 1
        WHERE id_livro = \''''+str(livro)+'''\'
        AND
        LIVROS.id = \''''+str(livro)+'''\'
        '''
    )
