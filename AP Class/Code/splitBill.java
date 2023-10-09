public class splitBill {
    public double divideBill(int numFriends, double bill)
    {
        double perFriend = bill / numFriends;
        return perFriend;
    }
    public static void main(String args[])
    {
        splitBill billMethod = new splitBill();
        double result = billMethod.divideBill(3, 5);
        System.out.print("Each Friend Should Pay $" + result);
    }
}
/** 
 * @author JudahStarkenburg
 * 
 * 
*/
