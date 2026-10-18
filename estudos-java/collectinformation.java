import java.util.Scanner;

public class collectinformation {
    public static void main (String[] arg ) {
        Scanner scanner = new Scanner (System.in);
            System.out.print("Insert your name:"); 
            String name = scanner.nextLine();
            // "nextLine" read and capture all line

            System.out.print("Insert a letter (just will accepted one letter):");
            char letter = scanner.next().charAt(0);
            //if I write "charAt(0)" the code just will collect the first letter/number


            System.out.println("Your name is:" + name);
            System.out.println("The first word is:" + letter);

        //close the scanner to can access another tools
        scanner.close();
    }
}

// Others input types:
// "nextInt": reed a number;
// "nextDouble": reed a decimal number;
// "nextBoolean": reed a boolean value (true or false).