public class DecimalSeparatorFormatter implements NumberFormatter {
    @Override
    public String format(int n) {
        return String.format("%,d", n);
    }
}
