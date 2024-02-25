class Billfold {
    private Card card1;
    private Card card2;

    public void addCard(Card card) {
        if (card1 == null) {
            card1 = card;
        } else if (card2 == null) {
            card2 = card;
        }
    }

    public String formatCards() {
        String card1String = (card1 != null) ? card1.format() : "";
        String card2String = (card2 != null) ? "|" + card2.format() : "";
        return "[" + card1String + card2String + "]";
    }

    public int getExpiredCardCount() {
        int count = 0;
        if (card1 != null && card1.isExpired()) {
            count++;
        }
        if (card2 != null && card2.isExpired()) {
            count++;
        }
        return count;
    }
}