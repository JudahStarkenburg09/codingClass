public class ArrayManipulation {
    public static void main(String[] args) {
        Integer[] a = { 1, 2, 3, 4, 5, 6, 7 };
        Character[] b = { 'a', 'b', 'c', 'd', 'e', 'f', 'g' };
        Double[] c = { 1.0, 2.0, 3.3, 4.4, 5.9, 8.7 };

        System.out.println("Original arrays:");
        print(a);
        print(b);
        print(c);

        System.out.println("\nReversed arrays:");
        reverse(a);
        reverse(b);
        reverse(c);

        System.out.println("\nArrays after reversal:");
        print(a);
        print(b);
        print(c);
    }

    public static <T> void print(T[] array) {
        for (T element : array) {
            System.out.print(element + " ");
        }
        System.out.println();
    }

    public static <T> void reverse(T[] array) {
        int left = 0;
        int right = array.length - 1;

        while (left < right) {
            // Swap elements at left and right indices
            T temp = array[left];
            array[left] = array[right];
            array[right] = temp;

            // Move left index to the right and right index to the left
            left++;
            right--;
        }
    }
}
