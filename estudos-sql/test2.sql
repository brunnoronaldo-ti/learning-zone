create table posts ( -- criação da tabela posts
    id serial primary key,
    titulo varchar(200),
    conteudo text,
    autor varchar(100),
    data_publicacao date
);

SELECT * -- Seleciona todas as colunas
FROM posts -- Seleciona todos os posts
WHERE autor = 'brunno' -- Filtra os posts do autor 'brunno'
ORDER BY data_publicacao DESC; -- Lista todos os posts do autor 'brunno', ordenados pela data de publicação mais recente

INSERT INTO posts (titulo, conteudo, autor, data_publicacao) -- Insere um novo post na tabela posts
VALUES ('Meu primeiro post', 'Este é o conteúdo do meu primeiro post.', 'brunno', '2024-06-01'); -- Adiciona um novo post
