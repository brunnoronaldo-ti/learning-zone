  programa
{
    funcao inicio()
    {
        real numero1, numero2, resultado
        cadeia operacao
        
        escreva("Digite o primeiro número: ")
        leia(numero1)
        
        escreva("Digite a operação (+, -, *, /): ")
        leia(operacao)
        
        escreva("Digite o segundo número: ")
        leia(numero2)
        
        escolha (operacao)
        {
            caso "+":
                resultado = numero1 + numero2
                escreva("Resultado: ", resultado, "\n")
                pare
            
            caso "-":
                resultado = numero1 - numero2
                escreva("Resultado: ", resultado, "\n")
                pare
            
            caso "*":
                resultado = numero1 * numero2
                escreva("Resultado: ", resultado, "\n")
                pare
            
            caso "/":
                se (numero2 != 0) {
                    resultado = numero1 / numero2
                    escreva("Resultado: ", resultado, "\n")
                } senao {
                    escreva("Erro: Divisão por zero!\n")
                }
                pare
            
            caso contrario:
                escreva("Operação inválida!\n")
        }
    }
}
               