// Judah Starkenburg
// 12/22/2023
// AP Computer Science A A


import java.util.Scanner;
import java.util.Random;

public class MovieTheater {

    public int[][] sell(String chosen, int[][] pattern) {


        System.out.println("Ticket sold for seat: " + chosen);

        int row = chosen.charAt(0) - 'A';
        int col = Integer.parseInt(chosen.substring(1)) - 1; 
        pattern[row][col] = 00;

        return pattern;

    }

    public int[][] chooseByPrice(int price, int[][] pattern) {

        Random random = new Random();
        int availableSeats = 0;

        for (int i = 0; i < pattern.length; i++) {
            for (int j = 0; j < pattern[i].length; j++) {
                if (pattern[i][j] == price) {
                    availableSeats++;
                }
            }
        }

        if (availableSeats > 0) {
            int randomSeat = random.nextInt(availableSeats) + 1;
            int seatCounter = 0;
            for (int i = 0; i < pattern.length; i++) {
                for (int j = 0; j < pattern[i].length; j++) {
                    if (pattern[i][j] == price) {
                        seatCounter++;
                        if (seatCounter == randomSeat) {
                            System.out.println("Ticket sold for seat: " + (char) ('A' + i) + (j + 1));
                            pattern[i][j] = 0;
                            return pattern;
                        }
                    }
                }
            }
        }

        System.out.println("No available seats with the specified price.");
        return pattern;
    }


    public void display(int[][] pattern) {
        System.out.print("    ");
        for (int col = 1; col <= pattern[0].length; col++) {
            System.out.printf("%2d ", col);
        }
        System.out.println();

        char rowLabel = 'A';

        for (int i = 0; i < pattern.length; i++) {
            System.out.print(rowLabel + " | ");

            for (int j = 0; j < pattern[i].length; j++) {
                if (pattern[i][j] == 0) {
                    System.out.print("XX ");
                } else {
                    System.out.printf("%02d ", pattern[i][j]);
                }
            }
            System.out.println();
            rowLabel++;
        }
    }



    public static void main(String[] args) {
        int[][] pattern = {
            {10, 10, 10, 10, 10, 10, 10, 10, 10, 10},
            {10, 10, 10, 10, 10, 10, 10, 10, 10, 10},
            {10, 10, 10, 10, 10, 10, 10, 10, 10, 10},
            {10, 10, 20, 20, 20, 20, 20, 20, 10, 10},
            {10, 10, 20, 20, 20, 20, 20, 20, 10, 10},
            {10, 10, 20, 20, 20, 20, 20, 20, 10, 10},
            {20, 20, 30, 30, 40, 40, 30, 30, 20, 20},
            {20, 30, 30, 40, 50, 50, 40, 30, 30, 20},
            {30, 40, 50, 50, 50, 50, 50, 50, 40, 30}
        };

        MovieTheater movieTheater = new MovieTheater();
        movieTheater.display(pattern);

        boolean running = true;
        Scanner scanner = new Scanner(System.in);
        while (running) {

            System.out.print("Press 1 To Choose Seat From Price, Press 2 To Choose From Row And Column: ");
            int choose = scanner.nextInt();

            if (choose == 1) {
                System.out.print("Enter The Price Of The Seat You Would Like To Sit In: ");
                int chosenPrice = scanner.nextInt();
                scanner.nextLine();
                System.out.println("\n\n\n\n\n");
                pattern = movieTheater.chooseByPrice(chosenPrice, pattern);
                movieTheater.display(pattern);
            } else if (choose == 2) {
                System.out.print("Enter The Row And Column That You Would Like To Sit In (A1-I10): ");
                scanner.nextLine();
                String chosen = scanner.nextLine();
                System.out.println("\n\n\n\n\n");
                pattern = movieTheater.sell(chosen, pattern);
                movieTheater.display(pattern);
            } else {
                running = false;
                scanner.close();
            }
            System.out.println("\n\n");
        }
    }
}
