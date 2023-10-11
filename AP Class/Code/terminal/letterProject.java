

public class letterProject {
    String recipient = "John";
    String greeting = "Dear ";
    String body = """
            How have you been? 
        """;
    String closing = "Take Care!";

    public void writeLetter() {
        greet();
        printBody();
        printClosing();
    }

    public void greet() {
        System.out.println(greeting + recipient + ",");
    }

    public void printBody() {
        System.out.println(body);
    }

    public void printClosing() {
        System.out.println(closing);
    }


    public static void main(String[] args) {

        letterProject friendLetter = new letterProject();
        friendLetter.writeLetter();
    }
}
