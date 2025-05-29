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

    static void Main()
    {
        Console.WriteLine("n;T(n)");
        for (int n = 200_000_000; n <= 1_000_000_000; n += 200_000_000)
        {
            int[] nums = new int[n];
            for (int i = 0; i < n; i++)
                nums[i] = 1;  // Worst: i    Best: 1
            for (int i = 0; i < 10; i++)
            {
                Stopwatch stopwatch = Stopwatch.StartNew();
                int x_max = FindMax(nums);
                stopwatch.Stop();
                double t = stopwatch.Elapsed.TotalSeconds;
                Console.WriteLine($"{n};{t:F10}".Replace(',', '.'));
            }
        }
    }
}

// (c) Valentin Arkov