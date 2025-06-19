using System;
class Program {
    static void BubbleSort(int[] arr) {
        int n = arr.Length;
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - i - 1; j++)
                if (arr[j] > arr[j + 1])
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j]);
    }
    static void Main() {
        int[] x = { 3, 2, 1, 4, 5 };
        Console.WriteLine(string.Join(" ", x));
        BubbleSort(x);
        Console.WriteLine(string.Join(" ", x));
    }
}

// (c) Valentin Arkov