import java.util.*;

public class Week26Lab {
    private static final String[] LETTERS = {
            "0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"
    };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a phone number: ");
        String phoneNumber = scanner.nextLine();

        List<String> spellings = generateSpellings(phoneNumber);
        System.out.println("Possible spellings:");
        for (String spelling : spellings) {
            System.out.println(spelling);
        }
    }

    public static List<String> generateSpellings(String phoneNumber) {
        List<String> result = new ArrayList<>();
        generateSpellingsHelper(phoneNumber, 0, "", result);
        return result;
    }

    private static void generateSpellingsHelper(String phoneNumber, int index, String currentSpelling, List<String> result) {
        if (index == phoneNumber.length()) {
            result.add(currentSpelling);
            return;
        }

        char digit = phoneNumber.charAt(index);
        int digitValue = Character.getNumericValue(digit);
        String letters = LETTERS[digitValue];
        
        for (int i = 0; i < letters.length(); i++) {
            char letter = letters.charAt(i);
            generateSpellingsHelper(phoneNumber, index + 1, currentSpelling + letter, result);
        }
    }
}
