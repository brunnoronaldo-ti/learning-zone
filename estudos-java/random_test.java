import java.util.Random;

public class random_test {
    public static void main(String[] args) {
        Random random = new Random();

        // Número inteiro aleatório (qualquer valor do tipo int)
        int numInteiro = random.nextInt();

        // Número inteiro entre 0 (inclusive) e 10 (exclusivo, ou seja, de 0 a 9)
        int numAteDez = random.nextInt(100,1000);

        // Número decimal entre 0.0 (inclusive) e 1.0 (exclusivo)
        double numDecimal = random.nextDouble();

        // Valor booleano aleatório (true ou false)
        boolean valorBool = random.nextBoolean();

        System.out.println("Inteiro: " + numInteiro);
        System.out.println("Between a specific pause: " + numAteDez);
        System.out.println("Decimal: " + numDecimal);
        System.out.println("Booleano: " + valorBool);
    }
}
