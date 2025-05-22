using System;
using System.Diagnostics;

class Program
{
    static int FindMax(int[] nums)
    {
        int max = nums[0];
        for (int i = 1; i < nums.Length; i++)
            if (max < nums[i])
                max = nums[i];
        return max;
    }

    static void Main()
    {
        Console.WriteLine("n;T(n)");
        for (int n = 100_000_000; n <= 300_000_000; n += 50_000_000)
        {
            int[] nums = new int[n];
            for (int i = 0; i < n; i++)
                nums[i] = 1;
            for (int i = 0; i < 10; i++)
            {
                Stopwatch stopwatch = Stopwatch.StartNew();
                int x_max = FindMax(nums);
                stopwatch.Stop();
                Console.WriteLine($"{n};{stopwatch.Elapsed.TotalSeconds:F10}");
            }
        }
    }
}
