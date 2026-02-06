
/*
1.SELECT
2.WHERE
3.INSERT
4.UPDATE
5.DELETE
6.ORDER BY
7.LIMIT
8.JOIN (boss)
*/

/* estrutura básica de um SELECT 

SELECT coluna (nome, idade, etc)
FROM tabela (nome_da_tabela, clientes, produtos, etc)
WHERE condição; (opcional)

*/

create table funcionarios (
    id serial primary key,
    nome varchar(100),
    idade int,
    cargo varchar(100),
    salario decimal
);

SELECT * 
FROM funcionarios
where idade > 18
ORDER BY idade DESC;

