--WELCOME TO CHALLENGE (this is just another exercise )
-- this file contains comments for record

-- 1. CREATE STRUCTURE  (DDL)
CREATE TABLE autores (
    -- id -> this is like an "ID card" for the row. almost all tables have one
    id SERIAL PRIMARY KEY,  -- primary key = This ID is unique. cannot exist two "autores" with same ID
    nome VARCHAR(100) NOT NULL -- this is small text (characters, symbols, numbers)
    -- another possibility is "TEXT", TEXT doesn't have limit. this is nice possibility for post content
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor_id INTEGER REFERENCES autores(id)  --integer - just whole numbers. we use in "autor_id" because he will keep the ID number
    /*This is the Foreign Key. It ensures integrity:
     you cannot create a post for an author_id = 99 if there is no author with ID 99 in the other table.
    */
);

-- 2. POPULATING (DML)
INSERT INTO autores (nome) VALUES ('Brunno'), ('Ana');

INSERT INTO posts (titulo, autor_id) VALUES 
('Meu primeiro post', 1), 
('SQL é massa', 1),
('Dicas de Django', 2);

--3. THE ANSWERS TO THE CHALLENGE
-- Question: Which posts did each author write?
SELECT autores.nome, posts.titulo
FROM autores
JOIN posts ON autores.id = posts.autor_id;

-- Question: How many posts does each author have?
SELECT autores.nome, COUNT(posts.id) AS total --COUNT(posts.id): It's a function that counts the lines.
-- AS total: Just an alias so the result column doesn't have the ugly name "count".
FROM autores
LEFT JOIN posts ON autores.id = posts.autor_id
GROUP BY autores.nome;
/*GROUP BY autores.nome: 
In SQL, you cannot "count" and "list names" simultaneously without grouping.
 The GROUP BY statement joins all rows from "Brunno" into one and applies the count to them.
*/
