using System;

namespace Lab4
{
    class Program
    {
        static void Main(string[] args)
        {
            Matrix matrix = new Matrix(6, 6);
            double[,] arr = new double[6, 6];
            for (int i = 0; i < arr.GetLength(0); i++)
            {
                for (int j = 0; j < arr.GetLength(1); j++)
                    matrix[i, j] = Func(double.Parse((i + 1).ToString()), double.Parse((j + 1).ToString()));
            } 
            Console.WriteLine("Matrix:");
            Matrix.ShowMatrix(matrix);
            Console.WriteLine("Evklid norm: " + EvklidNorm(matrix.data));
        }

        public static double Func(double i, double j)
        {
            double N = 2.0;
            return 125.0 / Math.Pow((4.0 + (0.1 * N * i * j * 0.25)), 6.0);
        }
        public static double EvklidNorm(double[,] matrix)
        {
            double powSum = 0;
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                    powSum += Math.Pow(Math.Abs(matrix[i, j]), 2.0);
            }
            return Math.Pow(powSum, 0.5);
        }
        // public static double ConditionNumber(double[])
        // {
        //     
        // }
        // def func(i, j):
        //     return 125 / ((4 + 0.1 * N * i * j * 0.25) ** 6);
        //
        // N = 2
        // n = 6
        // A = np.zeros((n, n))
        // for i in range(n):
        //     for j in range(n):
        //     A[i, j] = func(i + 1, j + 1)
        // print(A)
    }
}
