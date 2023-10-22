import javax.swing.JComponent;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.Color;

public class RectangleComponent extends JComponent
{
    public void paintComponent(Graphics g)
    {
        // Recover Graphics2D
        Graphics2D g2 = (Graphics2D) g;

        // Construct a rectangle and draw it with a center of 20, 20 (x = (desiredCenterX) - width/2), (y = (desiredCenterY) - height/2)
        Rectangle square1 = new Rectangle(0, 0, 40, 40);
        Rectangle square2 = square1;
        // Color yellow = new Color(255, 255, 0);

        g2.setColor(Color.RED);
        g2.draw(square2);

    }

}

