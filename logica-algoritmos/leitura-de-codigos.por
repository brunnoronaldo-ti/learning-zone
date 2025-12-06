Algoritmo "semnome"

Var
 codigo, quantidade : inteiro
 total : real

Inicio
   escreva("INSIRA O CÓDIGO:")
   leia(codigo)
   escreva("INSIRA A QUANTIDADE:")
   leia(quantidade)
   se codigo = 1 entao
    total <- 5.00 * quantidade
    escreval ("O VALOR É: ", total)
   senao
    se codigo = 2 entao
      total <- 3.50 * quantidade
      escreval ("O VALOR É: ", total)
     senao
     se codigo = 3 entao
       total <- 4.80 * quantidade
       escreval ("O VALOR É: ", total)
     senao
      se codigo = 4 entao
        total <- 8,90 * quantidade
        escreval ("O VALOR É: ", total)
      senao
       se codigo = 5 entao
         total <- 7.32 * quantidade
         escreval ("O VALOR É: ", total)
       fimse
      fimse
     fimse
    fimse
   fimse

   escreval("OBRIGADO PELA COMPRA")
Fimalgoritmo
