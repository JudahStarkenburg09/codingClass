public class inputsOutputs {
    public void calculate(double num1, double num2) {
        double average = ((num1 + num2)/2);
        System.out.println("The average of " + num1 + " and " + num2 + " is " + average);
    }

    public static void main(String[] args) {
        inputsOutputs calcAverage = new inputsOutputs();
        calcAverage.calculate(5, 10);
    }

}
