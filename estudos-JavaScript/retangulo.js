const base = number(prompt("Digite a base do retângulo:"));
const altura = number(prompt("Digite a altura do retângulo:"));

const area = base * altura;
const perimetro = 2 * (base + altura);

console.log("A área do retângulo é: " + area);
console.log("O perímetro do retângulo é: " + perimetro);
console.log("A diagonal do retângulo é: " + Math.sqrt(base**2 + altura**2));

console.log("Digite 1 para verificar se o retângulo é um quadrado ou 2 para sair:");
const escolha = number(prompt());
console.log();

if (escolha === 1) {
    if (base !== altura) {
        console.log("O retângulo não é um quadrado.");
        console.log();
        console.log("Redirecionando para saída...");
    }
    else {
        console.log("O retângulo é um quadrado.");
        console.log();
        console.log("Redirecionando para saída...");
    }
}
else if (escolha === 2) {
    console.log("Saindo...");
}
else {
    console.log("Opção inválida. redirecionando para saída...");
}
