public class Square
{
    private int sideLength;
    private int area;

    public makeSquare(int initialLength)
    {
       sideLength = initialLength;
       area = sideLength * sideLength;
    }

    public int getArea()
    {
       return area;
    }

    public void grow()
    {
       sideLength = 2 * sideLength;
    }
    public static void main(String[] args) {
        Square square = new Square();
        square.grow();
        square.makeSquare(5);
        System.out.println(square.getArea());
    }
}