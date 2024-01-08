import java.util.Scanner;

public class ZipCodeEncoder {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a five-digit ZIP code: ");
        String zipCode = scanner.nextLine();

        if (zipCode.length() != 5 || !zipCode.matches("\\d+")) {
            System.out.println("Invalid ZIP code. Please enter a valid five-digit ZIP code.");
            return;
        }

        int checkDigit = calculateCheckDigit(zipCode);

        String barcode = generateBarcode(zipCode + checkDigit);
        System.out.println("Barcode for " + zipCode + ": " + barcode);
    }

    private static int calculateCheckDigit(String zipCode) {
        int sum = 0;
        for (int i = 0; i < zipCode.length(); i++) {
            sum += Character.getNumericValue(zipCode.charAt(i));
        }
        return (10 - (sum % 10)) % 10;
    }

    private static String generateBarcode(String fullZipCode) {
        StringBuilder barcode = new StringBuilder("|");

        for (int i = 0; i < fullZipCode.length(); i++) {
            int digit = Character.getNumericValue(fullZipCode.charAt(i));
            barcode.append(encodeDigit(digit));
        }

        barcode.append("|"); 

        return barcode.toString();
    }

    private static String encodeDigit(int digit) {
        String[] encodingTable = {
                "||:::",
                ":::||",
                "::|:|",
                "::||:",
                ":|::|",
                ":|:|:",
                ":||::",
                "|:::|",
                "|::|:",
                "|:|::"
        };

        return encodingTable[digit];
    }
}
