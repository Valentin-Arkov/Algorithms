import java.util.Arrays;

public class Maxx {
    // Find maximum in array (built-in)
    static int findMax(int[] nums) {
        return Arrays.stream(nums).max().orElse(Integer.MIN_VALUE);
    }
    public static void main(String[] args) {
        int n = 40_000_000;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = 1;  // Best: 1   Worst: i
        }

        long t0 = System.nanoTime();
        int x_maxx = findMax(nums);
        long t1 = System.nanoTime();
        double t = (t1 - t0) / 1_000_000_000.0;
        System.out.println(n + " " + t);
    }
}
// (c) Valentin Arkov
