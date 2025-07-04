import java.util.Arrays;

public class merge3 {
    public static void main(String[] args) {
		System.out.println("n;T(n)");
        for (int n = 1_000_000; n < 10_000_001; n += 1_000_000) {
			int[] x = new int[n];
			for (int i = 0; i < n; i++) {
				x[i] = n - i;
			}
            for (int ii = 0; ii < 10; ii++) {
				long startTime = System.nanoTime();
				sort(x);
				long endTime = System.nanoTime();
				double duration = (endTime - startTime) / 1e9;
				System.out.println(n + "; " + String.format("%.10f", duration));
			}
		}
    }

    public static int[] sort(int[] x) {
        if (x.length < 2) {
            return x;
        } else {
            int mid = x.length / 2;
            int[] left = sort(Arrays.copyOfRange(x, 0, mid));
            int[] right = sort(Arrays.copyOfRange(x, mid, x.length));
            return merge(left, right);
        }
    }

    public static int[] merge(int[] left, int[] right) {
        int[] result = new int[left.length + right.length];
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                result[k] = left[i];
                i++;
            } else {
                result[k] = right[j];
                j++;
            }
            k++;
        }
        while (i < left.length) {
            result[k] = left[i];
            i++;
            k++;
        }
        while (j < right.length) {
            result[k] = right[j];
            j++;
            k++;
        }
        return result;
    }
}

//    100_000; 0,0139216000
//  1_000_000; 0,1327564000
// 10_000_000; 0,9417941000