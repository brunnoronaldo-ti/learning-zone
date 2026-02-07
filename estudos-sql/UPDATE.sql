-- never use UPDATE or DELETE without a SELECT 
-- nunca use UPDATE ou DELETE sem um SELECT

--UPDATE EXAMPLE

SELECT *
FROM funcionarios
WHERE cargo = 'Estagiário';

UPDATE funcionarios
SET salario = 1500
WHERE cargo = 'Estagiário';


-- tradução: Atualiza o salário dos funcionários com o cargo de 'Estagiário' para 1500
-- translation: update the salary of employees with the position of 'Estagiário' to 1500


/*update my mind

UPDATE funcionarios
SET salario = salario * 1.1
WHERE idade >= 25;

-- tradução: Atualiza o salário dos funcionários com idade maior ou igual a 25 anos, aumentando em 10%
-- translation: Update the salary of employees aged 25 or older, increasing it by 10%

*/


