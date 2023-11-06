public class VendingMachine
{
    private int canCount = 0;
    private int tokenCount = 5;
    private int inventory = 0;
    public void fillUp(int cans)
    {
        canCount += cans;
    }
    public void insertToken()
    {
        // each can costs 1 token
        tokenCount -= 1;
        canCount -= 1;
        inventory += 1;
    }
    public int getTokenCount()
    {
        return tokenCount;
    }
    public int getCanCount()
    {
        return canCount;
    }
    public int getInventory()
    {
        return inventory;
    }
     public static void main(String[] args)
   {
      VendingMachine machine = new VendingMachine();
      machine.fillUp(10); // Fill up with ten cans
      machine.insertToken();
      machine.insertToken();
      System.out.print("Token count: ");
      System.out.println(machine.getTokenCount());
      System.out.println("Expected: 3");
      System.out.print("Can count: ");
      System.out.println(machine.getCanCount()); 
      System.out.println("Expected: 8");
      System.out.print("You have bought ");
      System.out.println(machine.getInventory() + " cans!");
      System.out.println("Expected: 2");
   } 
}