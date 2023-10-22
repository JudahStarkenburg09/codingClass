import javax.swing.JComponent;
import java.awt.Graphics;
import java.awt.Graphics2D;

public class TextComponent extends JComponent
{
    public void paintComponent(Graphics g)
    {
        // Recover Graphics2D
        Graphics2D g2 = (Graphics2D) g;
        g2.drawString("Hello Dave", 95, 95);
    }

}

