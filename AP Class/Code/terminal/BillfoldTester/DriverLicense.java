import java.util.Calendar;
import java.util.GregorianCalendar;



class DriverLicense extends Card {
    private int expirationYear;

    public DriverLicense(String n, int expYear) {
        super(n);
        expirationYear = expYear;
    }

    public boolean isExpired() {
        GregorianCalendar calendar = new GregorianCalendar();
        int currentYear = calendar.get(Calendar.YEAR);
        return expirationYear < currentYear;
    }

    public String format() {
        return super.format() + " [Expiration year=" + expirationYear + "]";
    }

    public String toString() {
        return "DriverLicense[name=" + getName() + "][expirationYear=" + expirationYear + "]";
    }

    public boolean equals(Object obj) {
        if (obj == null) return false;
        if (getClass() != obj.getClass()) return false;
        DriverLicense other = (DriverLicense) obj;
        return getName().equals(other.getName()) && expirationYear == other.expirationYear;
    }
}