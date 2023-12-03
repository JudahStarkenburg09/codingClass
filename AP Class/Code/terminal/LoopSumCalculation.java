import java.util.Scanner;

public class LoopSumCalculation {
    // Function to calculate the sum of 1 + 2 + ... + n using a for loop
    public static int sumUsingFor(int n) {
        int total = 0;
        for (int i = 1; i <= n; i++) {
            total += i;
        }
        return total;
    }

    // Function to calculate the sum of 1 + 2 + ... + n using a while loop
    public static int sumUsingWhile(int n) {
        int total = 0;
        int i = 1;
        while (i <= n) {
            total += i;
            i++;
        }
        return total;
    }

    // Function to calculate the sum of 1 + 2 + ... + n using a do-while loop
    public static int sumUsingDoWhile(int n) {
        int total = 0;
        int i = 1;
        do {
            total += i;
            i++;
        } while (i <= n);
        return total;
    }

    public static void main(String[] args) {
        // Prompt user for input
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the max integer value: ");
        int maxValue = scanner.nextInt();

        // Calculate and print the sum using for loop
        int resultFor = sumUsingFor(maxValue);
        System.out.println("Sum using for loop: " + resultFor);

        // Calculate and print the sum using while loop
        int resultWhile = sumUsingWhile(maxValue);
        System.out.println("Sum using while loop: " + resultWhile);

        // Calculate and print the sum using do-while loop
        int resultDoWhile = sumUsingDoWhile(maxValue);
        System.out.println("Sum using do-while loop: " + resultDoWhile);
    }
}
