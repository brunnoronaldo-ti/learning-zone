using system;

//note¹: escreva/escreval = Console.Write / Console.WriteLine. (from library "using System;")
//note²: for print "." instead of "," as a decimal separator, use: CultureInfo.InvariantCulture (from library "using System.Globalization")

namespace name{ 
    class teste1{
        static void main(string[] args) {
            
            int idade; //whole number
            double salario, altura; //real
            char genero; //a single character
            string nome; //text (character)

            /* you can make this with another form:
                 int idade = 21;
                 string nome = "maria";
            */

            idade = 21;
            salario = 4550.0;
            altura = 1.71;
            genero = 'F'; // single character need single quotes
            nome = "maria";

            console.WriteLine(idade);
            console.WriteLine(salario);
            console.WriteLine(altura);
            console.WriteLine(genero);
            console.WriteLine(nome);
        }
    }
}
