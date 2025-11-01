Algoritmo "menu de interações-portugol"

   //um programa que simula um site
   //feito para experimentar funções
   
Var
   //divido pela categoria
   opcao, idade, senha, conf_senha, op_moeda : inteiro
   nome : caractere
   peso, altura, imc, alt2 : real
   mreal, mdolar, resultado : real

Inicio

   
   

   escreval("......login......")
   escreval()
   escreva("insira seu nome:")
   leia(nome)
   escreva("insira sua idade:")
   leia(idade)
   escreval("defina sua senha:")
   leia(senha)
   escreval("confirme sua senha:")
   leia(conf_senha)
   

   enquanto conf_senha <> senha faca
      escreval("senha incorreta!!")
      escreval("digite a senha novamente")
      leia (conf_senha)
   fimenquanto
   
   escreval()
   escreval("seja bem vindo senhor(a)", nome)
   escreval()
   
   enquanto opcao <> 4 faca
      escreval("o'que deseja fazer agora?")
      escreval("digite 1 para acessar a calculadora de imc")
      escreval("digite 2 para acessar o conversor de moeda")
      escreval("digite 3 para acessar a sala de agradecimento")
      escreval("digite 4 para sair")
      leia(opcao)
      escreval()
      escreval()
      escreval()
      
      se opcao = 1 entao
         escreval("acessando a calculadora de imc")
         escreval("insira seu peso")
         leia(peso)
         escreval("insira sua altura")
         leia(altura)
         escreval(nome, "seu peso é de ", peso,"kg, e sua altura é de", altura)

         alt2 <- altura * altura
         imc <- peso / alt2
         
          se imc < 18 entao
            escreval("seu imc é ", imc:1:2)
            escreval("seu imc é abaixo do peso para alguem com ", idade, " anos")
            escreval()
            escreval()
         senao
            se imc < 24 entao
               escreval("seu imc é ", imc:1:2)
               escreval("seu imc é normal para alguem com ", idade, " anos")
               escreval()
               escreval()
            senao
               se imc < 29 entao
                  escreval("seu imc é", imc:1:2)
                  escreval("seu imc é de sobrepeso para alguem com ", idade, " anos")
                  escreval()
                  escreval()
               senao
                  escreval("seu imc é", imc:1:2)
                  escreval("seu imc é de obeso para alguem com ", idade, " anos")
                  escreval()
                  escreval()
               fimse
            fimse
         fimse
         //corrigir erro de loop aqui
         //atualização: erro corrigido
      senao
         se opcao = 2 entao
         //testar esse código
         //atualização: concertar bug
         //atualização: bug corrigido
            escreval("acessando conversor de moeda")
            escreval("qual moeda vocè vai converter?")
            escreval("1 = dolar")
            escreval("2 = real")
            leia(op_moeda)
            se op_moeda = 1 entao
               escreval()
               escreval("você escolheu o dólar, insira o valor")
               escreva("dólar:")
               leia(mdolar)
               
               resultado <- mdolar * 4,97
               escreval("a conversão de dólar para real é de: ",resultado:1:2)
               escreval()
               escreval()
            senao
               se op_moeda = 2 entao
               
                     escreval()
                     escreval("você escolheu o real, insira o valor")
                     escreva("real")
                     leia(mreal)
                     resultado <- mreal / 5,22
                     escreval("a conversão de real para dólar é de: ",resultado:1:2)
                     escreval()
                     escreval()
               senao
                  escreval("número inválido, insira outro")
                  escreval()
               fimse
            fimse
         senao
            se opcao = 3 entao
               se idade > 18 entao
                  escreval("essa linha é apenas uma linha de agradecimento")
                  escreval("obrigado por testar meu código")
                  //obrigado por lêr esse código
                  escreval()
                  escreval()
               senao
                  escreval("você é novo demais para acessar esse menu")
                  escreval()
                  escreval()
               fimse
            fimse
         fimse
      fimse
   fimenquanto
   
   escreval("saindo do programa")
   escreval("até mais")
Fimalgoritmo
