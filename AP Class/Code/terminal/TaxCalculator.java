/* 
* Judah Starkenburg
* Week 10 Lab
* AP CS A-A
* 11/19/2023
* Note: I was typing .equals, when I noticed .equalIgnoreCase, 
*       I don't think we learned this but I thought it would be useful for this project
*/



import java.util.Scanner;

public class TaxCalculator {

    public void ifStatements(double taxInput, double tax, String userInput) {
        // Check for if single
        if (userInput.equalsIgnoreCase("s")) { 
            // Check users income
            if (taxInput >= 0 && taxInput <= 8000) {
                tax = taxInput * .1;
            } 
            else if (taxInput > 8000 && taxInput <= 32000) {
                tax = 800 + ((taxInput - 8000) * .15);
            }
            else if (taxInput > 32000) {
                tax = 4400 + ((taxInput - 32000) * .25);
                
            }
            else {
                System.out.println("You are in debt");
            }
            System.out.println("You must pay $" + tax + " tax!");
        
        }
        // Check for if married
        else if (userInput.equalsIgnoreCase("m")) {
            // Check users income
            if (taxInput >= 0 && taxInput <= 16000) {
                tax = taxInput * .1;
            } 
            else if (taxInput > 16000 && taxInput <= 64000) {
                tax = 1600 + ((taxInput - 16000) * .15);
            }
            else if (taxInput > 64000) {
                tax = 8800 + ((taxInput - 64000) * .25);
                
            }
            else {
                System.out.println("You are in debt");
            }
            System.out.println("You must pay $" + tax + " tax!");
        }
    }



    public static void main(String[] args) {
        boolean running = true;
        TaxCalculator calculator = new TaxCalculator();
        while (running) {
            double taxInput = 0.0;
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter 's' for single, and 'm' for married ('end' to exit): "); // Accept Status
            String userInput = scanner.nextLine();

            // See if userInput does not equal s, m, or end (Invalid if so)
            if (! userInput.equalsIgnoreCase("s") && ! userInput.equalsIgnoreCase("m") && ! userInput.equalsIgnoreCase("end")) {
                System.out.println("Enter a valid status!");
            } // See if userInput equals end, (end loop if so)
            else if (userInput.equalsIgnoreCase("end")) {
                scanner.close();
                running = false;
            } // If no errors / No end loop, then ask for income
            else {
                System.out.print("Enter A Taxable Income: $");
                double tax = 0.0;
                
                // See if the taxable income is a double, if so, save it as taxInput, and run the if statments
                if (! scanner.hasNextDouble()) {
                    System.out.println("Please enter a Valid Integer!");
                }
                else { // Run the if statements after saving taxInput as a double
                    taxInput = scanner.nextDouble();
                    calculator.ifStatements(taxInput, tax, userInput);
                }
            }


            System.out.println("\n\n\n\n"); // Learned from python...
        }
    }
}
