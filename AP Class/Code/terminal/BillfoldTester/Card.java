public class Card {
    private String name;

    public Card() {
        name = "";
    }

    public Card(String n) {
        name = n;
    }

    public String getName() {
        return name;
    }

    public boolean isExpired() {
        return false;
    }

    public String format() {
        return "Card holder: " + name;
    }

    public String toString() {
        return "Card[name=" + name + "]";
    }

    public boolean equals(Object obj) {
        if (obj == null) return false;
        if (getClass() != obj.getClass()) return false;
        Card other = (Card) obj;
        return name.equals(other.name);
    }
}