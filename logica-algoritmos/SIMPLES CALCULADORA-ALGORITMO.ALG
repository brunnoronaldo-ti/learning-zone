Algoritmo "simples calculadora-algoritmo"
//um simples programa
Var
   a, b : inteiro
   total : real
   conta : caractere
   saida : caractere

Inicio
   escreval("para fechar o programa digite: SAIR")
   escreval()
   escreval("primeiramente insira os números e após insira o tipo da conta")
   escreval()
   
   enquanto saida <> "s" faca
      escreval("digite o primeiro número: ")
      leia(a)
      escreval("digite o segundo número: ")
      leia(b)
      escreval("escolha o tipo de conta:")
      
      
         escreval("!!insira apenas números inteiros!!")
     
      
      escreval("soma")
      escreval("subtração")
      escreval("multiplicação")
      escreval("divisão")
      escreval()
      leia(conta)
      escreval()
      
      se conta = "soma" entao
        total <- a + b
        escreval(a, " +", b, " =", total)
      senao
         se conta = "subtração" entao
            total <- a - b
            escreval(a, " -", b, " =", total)
         senao
            se conta = "multiplicação" entao
               total <- a * b
               escreval(a, " x", b, " =", total)
            senao
               se conta = "divisão" entao
                  total <- a / b
                  escreval(a, " %", b, " =", total)
               senao
                  escreval("")
               fimse
            fimse
         fimse
      fimse
      
      escreval("deseja sair? (s/n)")
      
      leia(saida)
         se saida = "s" entao
            escreval()
            escreval("saindo...")
         senao
            se saida = "n" entao
               escreval()
               escreval("retornando...")
               escreval()
            senao
               escreval("digite apenas S ou N")
               leia(saida)
            fimse
         fimse
      
   fimenquanto
   

Fimalgoritmo