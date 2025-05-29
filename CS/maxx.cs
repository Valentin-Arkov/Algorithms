using System;
using System.Diagnostics;
using System.Linq;

class Program
{
    // find maximum in array (built-in)
    static int FindMax(int[] nums)
    {
        return nums.Max();
    }

    static void Main(string[] args)
    {
        // Choose array size (0.1 ... 1 sec)
        int n = 1_000_000_000;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++)
            nums[i] = 1;   // Best case
            // nums[i] = i;      // Worst case

        Stopwatch stopwatch = Stopwatch.StartNew();
        int x_max = FindMax(nums);
        stopwatch.Stop();
        double t = stopwatch.Elapsed.TotalSeconds;

        Console.WriteLine($"{n} {t}");
    }
}

// (c) Valentin Arkov