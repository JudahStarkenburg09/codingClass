class CallingCard extends Card {
    private String cardNumber;
    private String pin;

    public CallingCard(String n, String number, String pin) {
        super(n);
        cardNumber = number;
        this.pin = pin;
    }

    public String format() {
        return super.format() + " [Card number=" + cardNumber + ", PIN=" + pin + "]";
    }

    public String toString() {
        return "CallingCard[name=" + getName() + "][number=" + cardNumber + ", pin=" + pin + "]";
    }

    // No need to override equals() from Card class as it compares only names
}