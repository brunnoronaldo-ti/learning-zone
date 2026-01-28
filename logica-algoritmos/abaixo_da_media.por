Algoritmo "abaixo_da_media"

Var
   vet : vetor [0..9] de inteiro
   n, i : inteiro
   soma, media : real

Inicio
   soma <- 0
   
   escreval("quantos elementos vai ter o vetor? ")
   leia(n)

   para i de 0 ate n-1 faca
      escreval("insira o números: ")
      leia(vet[i])
   fimpara
   
   escreval()
   escreval()

   para i de 0 ate n-1 faca
      soma <- soma + (vet[i])
   fimpara
   
   media <- soma / n
   
   escreval("média do vetor =", media)
   escreval("valores abaixo da média: ")
   
   para i de 0 ate n-1 faca
      se (vet[i]) < media entao
         escreval(vet[i])
      fimse
   fimpara
   
Fimalgoritmo
