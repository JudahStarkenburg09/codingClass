import javax.swing.JFrame;

public class call {
    public static void main(String[] args)
    {
        JFrame frame = new JFrame();
        frame.setSize(300, 400);
        frame.setTitle("Hello Dave");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        RectangleComponent Rcomponent = new RectangleComponent();
        frame.add(Rcomponent);
        frame.setVisible(true);
        ElipseComponent Ecomponent = new ElipseComponent();
        frame.add(Ecomponent);
        frame.setVisible(true);
        LineComponent Lcomponent = new LineComponent();
        frame.add(Lcomponent);
        frame.setVisible(true);
        TextComponent Tcomponent = new TextComponent();
        frame.add(Tcomponent);
        frame.setVisible(true);


    }
}
