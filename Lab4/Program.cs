using System;

namespace Lab4
{
    class Program
    {
        static void Main(string[] args)
        {
            Matrix matrix = new Matrix(3, 3);
            matrix[0, 0] = 1.0;
            matrix[0, 1] = 2.0;
            matrix[0, 2] = 3.0;
            matrix[1, 0] = 2.0;
            matrix[1, 1] = 3.0;
            matrix[1, 2] = 4.0;
            matrix[2, 0] = 3.0;
            matrix[2, 1] = 5.0;
            matrix[2, 2] = 4.0;
            //Matrix.ShowMatrix(Matrix.LUMatrix(matrix));
            //Console.WriteLine(Matrix.Det(matrix));
            Matrix.ShowMatrix(Matrix.GetL(matrix));
            Matrix matrix2= new Matrix(3, 3);
            matrix2[0, 0] = 1.0;
            matrix2[0, 1] = 2.0;
            matrix2[0, 2] = 3.0;
            matrix2[1, 0] = 2.0;
            matrix2[1, 1] = 3.0;
            matrix2[1, 2] = 4.0;
            matrix2[2, 0] = 3.0;
            matrix2[2, 1] = 5.0;
            matrix2[2, 2] = 4.0;
            Matrix.ShowMatrix(matrix2);
        }
    }
}
