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

const PossivelAcao = ['inimigo', 'npc', 'item', 'local', 'evento'];

const inimigos = [
    new inimigo("Goblin", 30, 5),
    new inimigo("Esqueleto", 40, 7),
    new inimigo("Zumbi", 50, 10)
]

const itens = [
    new item("Poção de Vida", "Restaura 20 pontos de vida"),
    new item("Poção de Sanidade", "Restaura 20 pontos de sanidade"),
    new item("Lanterna", "Aumenta a luz em 5")
]

const locais = [
    new local("Sala de Tesouro", "Uma sala cheia de riquezas e perigos"),
    new local("Biblioteca Abandonada", "Uma biblioteca antiga cheia de segredos"),
    new local("Caverna Escura", "Uma caverna profunda e perigosa")
]

const npcs = [
    new npc("Velho Sábio", "Fornece informações valiosas"),
    new npc("Mercador", "Vende itens úteis"),
    new npc("Guardião", "Protege um local importante")
]

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
            console.log("Você explora o andar e...")
                // Gerar um evento aleatório
                const evento = PossivelAcao[rolarDado(0, PossivelAcao.length - 1)];

                switch (evento) {
                    case 'inimigo':
                        console.log("Um inimigo surge!")
                        const inimigo_encontrado = inimigos[rolarDado(0, inimigos.length - 1)];
                        console.log("Você está enfrentando um " + inimigo_encontrado.nome + "!")
                        while (inimigo_encontrado.hp > 0 && vida > 0) {

                            //ação do herói
                            const acao = input.question("Escolha uma ação: 1. Atacar 2. Fugir: ")
                            if (acao === "1") {
                                const dano_heroi = rolarDado(5, 15);    
                                inimigo_encontrado.hp -= dano_heroi;
                                console.log("Você causa " + dano_heroi + " de dano no " + inimigo_encontrado.nome);
                            } else if (acao === "2") {
                                console.log("Você tenta fugir...")
                                if (rolarDado(1, 20) > 10) {
                                    console.log("Você conseguiu fugir!")
                                    break;
                                }
                                else {
                                    console.log("Você falhou em fugir!")
                                }
                            } else {
                                console.log("Ação inválida!")
                            }

                            //ação do inimigo
                            if (inimigo_encontrado.hp > 0) {
                                vida -= inimigo_encontrado.dano;
                                console.log("O " + inimigo_encontrado.nome + " causa " + inimigo_encontrado.dano + " de dano em você!")
                            }
                        }

                        break;
                    case 'npc':
                        console.log("Você encontra um NPC amigável!")
                        break;
                    case 'item':
                        console.log("Você encontra um item!")
                        break;
                    case 'local':
                        console.log("Você descobre um local interessante!")
                        break;
                    case 'evento':
                        console.log("Um evento inesperado acontece!")
                        break;
                }
        } else if (escolha === "2") {
            Game = false;
            break;
        } else {
            console.log("Opção inválida!")
        }

        

    }

}
