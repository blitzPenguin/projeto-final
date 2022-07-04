/* Criação da base de dados */
DROP DATABASE IF EXISTS Biblioteca_bd;
CREATE DATABASE Biblioteca_bd;

USE Biblioteca_bd;

/* Criação das tabelas */
CREATE TABLE ALUNOS (
	id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	id_turma INTEGER NOT NULL,
	email VARCHAR(100)
);

CREATE TABLE TURMAS (
	id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	designacao VARCHAR(5) NOT NULL
);

DROP TABLE IF EXISTS LIVROS;
CREATE TABLE LIVROS (
	id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	isbn INTEGER(10) NOT NULL,
	titulo VARCHAR(100) NOT NULL,
	autor VARCHAR(100) NOT NULL,
	editora VARCHAR(100) NOT NULL,
	data_publicacao YEAR NOT NULL,
	id_requisitado INTEGER NOT NULL DEFAULT '1',
	ativo BOOLEAN DEFAULT '1'
);

DROP TABLE IF EXISTS GENEROS;
CREATE TABLE GENEROS (
	id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	designacao VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS LIVROS_GENEROS;
CREATE TABLE LIVROS_GENEROS (
	id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_livro INTEGER NOT NULL,
	id_genero INTEGER NOT NULL
);

CREATE TABLE REQUISICOES_HEADER (
	id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_aluno INTEGER NOT NULL,
	data_req DATE NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	data_limite DATE NOT NULL
);

CREATE TABLE REQUISICOES_DESC (
	id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_requisicao INTEGER NOT NULL,
	id_livro INTEGER NOT NULL,
	devolvido BOOLEAN NOT NULL DEFAULT '0'
);

CREATE TABLE REQUISITADO (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    designacao VARCHAR(100)
);

/* Criação de chaves estrangeiras */
ALTER TABLE ALUNOS
	ADD CONSTRAINT FK_TURMAS_ALUNOS FOREIGN KEY(id_turma) REFERENCES TURMAS(id);

ALTER TABLE LIVROS
	ADD CONSTRAINT FK_LIVROS_REQUISITADO FOREIGN KEY(id_requisitado) REFERENCES REQUISITADO(id);

ALTER TABLE LIVROS_GENEROS
	ADD CONSTRAINT FK_LIVROS_LIVGEN FOREIGN KEY(id_livro) REFERENCES LIVROS(id),
	ADD CONSTRAINT FK_GENEROS_LIVGEN FOREIGN KEY(id_genero) REFERENCES GENEROS(id);

ALTER TABLE REQUISICOES_HEADER
	ADD CONSTRAINT FK_ALUNOS_REQHEAD FOREIGN KEY(id_aluno) REFERENCES ALUNOS(id);

ALTER TABLE REQUISICOES_DESC
	ADD CONSTRAINT FK_REQHEAD_REQDESC FOREIGN KEY(id_requisicao) REFERENCES REQUISICOES_HEADER(id),
	ADD CONSTRAINT FK_LIVROS_REQDESC FOREIGN KEY(id_livro) REFERENCES LIVROS(id);

/* Introdução de dados */

INSERT INTO TURMAS (designacao) VALUES	('9ºA'),
										('8ºB');

INSERT INTO ALUNOS (nome, id_turma, email) VALUES	('João', 1, 'joao@notmail.com'),
													('Pedro', 2, 'pedro@notmail.com');

INSERT INTO REQUISITADO (designacao) VALUES	('Não Requisitado'),
											('Requisitado');

INSERT INTO GENEROS (designacao) VALUES	('Terror'),
										('Comedia'),
                                        ('Drama'),
                                        ('Romance'),
                                        ('Fantasia');

INSERT INTO LIVROS (isbn, titulo, autor, editora, data_publicacao, id_requisitado) VALUES
    (123456789, 'O Senhor dos Anéis', 'J.R.R. Tolkien', 'Minha Biblioteca', 1954, 2),
    (234567891, 'A Arte da Guerra', 'Sun Tzu', 'Editora chinas', 1980, 1),
    (345678912, 'Os Maias', 'Eça de Queiroz', 'Porto Editora', 1985, 1),
    (456789123, 'Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 'Editorial Presença', 1997, 1);

INSERT INTO LIVROS_GENEROS (id_livro, id_genero) VALUES (1, 1),
                                                        (1, 5),
                                                        (2, 2),
                                                        (3, 3),
                                                        (3, 4),
                                                        (4, 4);

INSERT INTO REQUISICOES_HEADER (id_aluno, data_limite) VALUES (1, '2020-01-01');

INSERT INTO REQUISICOES_DESC (id_requisicao, id_livro, devolvido) VALUES (1, 1, 0);