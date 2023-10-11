public class assignment
{
      public static void main(String[] args)
      {
         // measurements in feet
             int w = 10;
             int L = 50;
             int h = 25;
             int nW = 2; // number of windows
             int nD = 1; // number of doors
             int sizeW = 5*5; // size windows (x,y)
             int sizeD = 3*8; // size doors (x,y)
             System.out.println("                     ");
             System.out.print("Your surface area is: ");
             System.out.print((w * L * h * 6) - ((nW * sizeW) + (nD * sizeD)));
             System.out.println("ft²");
             System.out.println("                     ");
      }
}
