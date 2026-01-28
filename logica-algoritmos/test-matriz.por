Algoritmo "execício-matriz"

Var
   n, j, i, media : inteiro
   mat : vetor [0..9, 0..9] de inteiro

Inicio
   escreval("qual a ordem da matriz?")
   leia(n)
   escreval()
   
   para i de 0 ate n-1 faca
      para j de 0 ate n-1 faca
         escreval("Elemento [", i, ",", j, "]: ")
         leia(mat[i, j])
      fimpara
   fimpara

   para i de 0 ate n-1 faca
      para j de 0 ate n-1 faca
         se (mat[i, j]) < 0 entao
            media <- media + 1
         fimse
      fimpara
   fimpara
Fimalgoritmo
