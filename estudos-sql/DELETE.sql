--DELETE EXAMPLE

SELECT *
FROM posts
WHERE autor = 'brunno';

DELETE FROM posts
WHERE autor = 'brunno';

-- tradução: Deleta todos os posts do autor 'brunno'
-- translation: Deletes all posts by the author 'brunno'

/*delete my mind
DELETE FROM funcionarios
WHERE idade < 18;
-- tradução: Deleta todos os funcionários com idade menor que 18 anos
-- translation: Deletes all employees under the age of 18
*/

/*
Sem WHERE = extinção em massa
DELETE não pede confirmação
Banco não tem pena
*/
