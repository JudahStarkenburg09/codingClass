import java.util.Calendar;
import java.util.GregorianCalendar;

public class BillfoldTester {
    public static void main(String[] args) {
        Billfold billfold = new Billfold();
        CallingCard callingCard = new CallingCard("Bjarne Stroustrup", "4156646425", "2234");
        DriverLicense driverLicense = new DriverLicense("John Doe", 2020); // Expired license

        billfold.addCard(callingCard);
        billfold.addCard(driverLicense);

        System.out.println("Number of expired cards: " + billfold.getExpiredCardCount());
        System.out.println("Formatted cards: " + billfold.formatCards());
    }
}
