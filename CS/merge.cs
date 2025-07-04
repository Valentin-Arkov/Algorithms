using System;

class MergeSort
{
    static void Main(string[] args)
    {
        Console.WriteLine("n;T(n)");
        for (int n = 1000000; n < 10000001; n += 1000000)
        {
            int[] x = new int[n];
            for (int i = 0; i < n; i++)
            {
                x[i] = n - i;
            }
            for (int ii = 0; ii < 10; ii++)
            {
                var watch = System.Diagnostics.Stopwatch.StartNew();
                Sort(x);
                watch.Stop();
                double duration = watch.Elapsed.TotalMilliseconds / 1000.0;
                Console.WriteLine(n + "; " + duration.ToString("0.0000000000"));
            }
        }
    }

    public static int[] Sort(int[] x)
    {
        if (x.Length < 2)
        {
            return x;
        }
        else
        {
            int mid = x.Length / 2;
            int[] left = Sort(new ArraySegment<int>(x, 0, mid).ToArray());
            int[] right = Sort(new ArraySegment<int>(x, mid, x.Length - mid).ToArray());
            return Merge(left, right);
        }
    }

    public static int[] Merge(int[] left, int[] right)
    {
        int[] result = new int[left.Length + right.Length];
        int i = 0, j = 0, k = 0;
        while (i < left.Length && j < right.Length)
        {
            if (left[i] <= right[j])
            {
                result[k] = left[i];
                i++;
            }
            else
            {
                result[k] = right[j];
                j++;
            }
            k++;
        }
        while (i < left.Length)
        {
            result[k] = left[i];
            i++;
            k++;
        }
        while (j < right.Length)
        {
            result[k] = right[j];
            j++;
            k++;
        }
        return result;
    }
}
