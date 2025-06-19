import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] x = {3, 2, 1, 4, 5};
        System.out.println(Arrays.toString(x));
        bubble(x);
        System.out.println(Arrays.toString(x));
    }

    private static void bubble(int[] x) {
        int n = x.length;
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - i - 1; j++)
                if (x[j] > x[j + 1]) {
                    int temp = x[j];
                    x[j] = x[j + 1];
                    x[j + 1] = temp;
                }
    }
}
// (c) Valentin Arkov