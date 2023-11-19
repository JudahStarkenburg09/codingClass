import java.util.Scanner;

public class TaxCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        while (running) {
            System.out.print("Enter 's' for single, and 'm' for married ('end' to exit): ");
            String userInput = scanner.nextLine();
            System.out.print("");

            if (userInput.equals("end")) {
                scanner.close();
                running = false;
            } 
            else if (userInput.equalsIgnoreCase("s")) { // I don't think we learned this, but as I was typing .equals, I saw .equalsIgnoreCase
                System.out.println("You are Single");
            }
            else if (userInput.equalsIgnoreCase("m")) {
                System.out.println("You are Married");
            }
            else {
                System.out.println("Please enter a valid statement!");
            }
        }
    }
}
