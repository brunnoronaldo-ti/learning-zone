/*JOIN conecta dados de duas ou mais tabelas com base
em uma coluna relacionada entre elas. Existem diferentes tipos de JOIN, como:
    INNER
    JOIN,
    LEFT
    JOIN,
    RIGHT
    JOIN
    FULL OUTER JOIN;
cada um com suas próprias regras de como os dados são combinados.
*/

CREATE TABLE autores ( -- criação da tabela autores
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) 
);

CREATE TABLE posts ( -- criação da tabela posts
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200),
    conteudo TEXT,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
);

/*
    -- JOIN na prática (exemple)

    SELECT posts.titulo, autores.nome
    FROM posts
    JOIN autores ON posts.autor_id = autores.id;
    -- tradução: Seleciona o título do post e o nome do autor, combinando as tabelas posts e autores com base na coluna autor_id que referencia a coluna id da tabela autores
    -- translation: Selects the post title and author name, combining the posts and authors tables based on the author_id column that references the id column of the authors table
*/


--just example

SELECT posts.titulo, autores.nome
FROM posts
JOIN autores ON posts.autor_id = autores.id;

--join with filter

SELECT posts.titulo, autores.nome
FROM posts
JOIN autores ON posts.autor_id = autores.id
WHERE autores.nome = 'Brunno';

-- JOIN + ORDER + LIMIT

SELECT posts.titulo, autores.nome
FROM posts
JOIN autores ON posts.autor_id = autores.id
ORDER BY posts.id DESC
LIMIT 3;


/* conection with DJANGO 

    Post.objects.select_related('autor').all()
*/

