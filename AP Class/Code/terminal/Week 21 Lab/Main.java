import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();
        
        NumberFormatter defaultFormatter = new DefaultFormatter();
        NumberFormatter decimalFormatter = new DecimalSeparatorFormatter();
        NumberFormatter accountingFormatter = new AccountingFormatter();
        
        System.out.println("Default Format: " + defaultFormatter.format(number));
        System.out.println("Decimal Separator Format: " + decimalFormatter.format(number));
        System.out.println("Accounting Format: " + accountingFormatter.format(number));
        
        scanner.close();
    }
}
