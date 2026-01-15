const nome = prompt("Qual seu nome?")
const idade = Number(prompt("Qual sua idade?"))
// utiizei "const" pois não pretendo mudar o valor dessas variáveis

console.log("Olá, " + nome + "! Você tem " + idade + " anos.")

if (idade < 18) {
    console.log("Você é menor de idade, falta " + (18 - idade) + " anos para ser maior de idade.")
} 
else {
    console.log("Você é maior de idade, daqui a um ano você terá " + (idade + 1) + " anos.")
}

