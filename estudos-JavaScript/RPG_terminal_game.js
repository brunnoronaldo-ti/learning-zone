// bibliotecas
const input = require('readline-sync');

// status mutaveis
let vida = 100
let sanidade = 100
let luz = 10
let Game = true
const d20 = Math.floor(Math.random() * 20) + 1;
const d6 = Math.floor(Math.random() * 6) + 1;
let andar_atual = 1

// informações

class personagem {
    constructor(nome, classe) {
        this.nome = nome;
        this.classe = classe;
    }
}

class inimigo {
    constructor(nome, hp, dano) {
        this.nome = nome;
        this.hp = hp;
        this.dano = dano;
    }
}

class item {
    constructor(nome, efeito) {
        this.nome = nome;
        this.efeito = efeito;
    }
}

class local {
    constructor(nome, descricao) {
        this.nome = nome;
        this.descricao = descricao;
    }  
}

class npc {
    constructor(nome, papel) {
        this.nome = nome;
        this.papel = papel;
    }
}

// O seu "random.randint(min, max)" personalizado
function rolarDado(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function iniciarjogo() {
    console.log("------ bem vindo ao jogo de RPG (JS) ------")

    //similar ao input do python, para receber dados do usuário
    const nomeheroi = input.question("Qual o nome do seu personagem? ")
    const classeheroi = input.question("Escolha a classe do seu personagem (Guerreiro, Mago, Arqueiro): ")
    const heroi = new personagem(nomeheroi, classeheroi);

    console.log("Olá, " + heroi.nome + "! Vamos começar a aventura!")

    while (Game) {
        console.log("Você está no andar " + andar_atual + ". O que deseja fazer?")
        console.log("1. Explorar o andar")
        console.log("2. sair do jogo")

        const escolha = input.question("Escolha uma opção: ")

        if (escolha === "1") {
            console.log("Você explora o andar e encontra um...")
        
        } else if (escolha === "2") {
            Game = false;
        } else {
            console.log("Opção inválida!")
        }

    }

}
