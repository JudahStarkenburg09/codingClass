
class IDCard extends Card {
    private String idNumber;

    public IDCard(String n, String id) {
        super(n);
        idNumber = id;
    }

    public String format() {
        return super.format() + " [ID number=" + idNumber + "]";
    }

    public String toString() {
        return "IDCard[name=" + getName() + "][ID number=" + idNumber + "]";
    }

    // No need to override equals() from Card class as it compares only names
}