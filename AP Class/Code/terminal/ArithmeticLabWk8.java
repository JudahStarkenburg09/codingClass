/** 
Judah Starkenburg Nov 11 2023
AP Computer Science A-A
Week 8 Arithmetic Lab 
**/

import java.util.Scanner;

public class ArithmeticLabWk8 {
    private int num1;
    private int num2;

    private void performOperations() {
        // Operations:
        int sum = num1 + num2;
        int difference = num1 - num2;
        int product = num1 * num2;
        double average = (double) sum / 2;
        int distance = Math.abs(difference);
        int max = Math.max(num1, num2);
        int min = Math.min(num1, num2);

        // Print statements
        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
        System.out.println("Product: " + product);
        System.out.println("Average: " + average);
        System.out.println("Distance: " + distance);
        System.out.println("Maximum: " + max);
        System.out.println("Minimum: " + min);
    }

    public static void main(String[] args) {
        // Input 25 and 20 to get same results as lab example
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first integer: ");
        int num1 = scanner.nextInt();
        System.out.print("Enter the second integer: ");
        int num2 = scanner.nextInt();

        ArithmeticLabWk8 arithmeticLab = new ArithmeticLabWk8();
        arithmeticLab.num1 = num1;
        arithmeticLab.num2 = num2;
        arithmeticLab.performOperations();
        scanner.close();
    }
}
