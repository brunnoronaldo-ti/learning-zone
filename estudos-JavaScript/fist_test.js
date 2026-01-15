//primeiro uso de javascript

/* Declaração de variáveis em JavaScript
 Utilizando let para declarar variáveis de diferentes tipos
 Número, String, Boolean, Array e Object 
 let é mutável 
 use const sempre, só use let quando precisar mudar o valor.
*/

let numero = 10
let texto = "salve"
let booleano = true
let lista = [1, 2, 3]
let objeto = { nome: "Brunno", idade: 19 }

/*
    exemplo de declaração de variáveis (usando const):

    const texto = "salve"
    const numero = 10
    const booleano = true
    const lista = [1, 2, 3]
    const objeto = { nome: "Brunno", idade: 19 }
*/

// Exibindo os valores no console
// Usando console.log para imprimir os valores das variáveis
console.log(numero)
console.log(texto)
console.log(booleano)
console.log(lista)
console.log(objeto)

// Modificando o valor da variável numero (exemplo de mutabilidade)
numero = 20
console.log("Número modificado:", numero)
