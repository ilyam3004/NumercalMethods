﻿using System;

namespace Lab4
{
    public class Matrix
    {
        private double[,] data;
        private double precalculatedDeterminant = double.NaN;

        private int m;

        public int M
        {
            get => this.m;
        }

        private int n;

        public int N
        {
            get => this.n;
        }

        public bool IsSquare
        {
            get => this.M == this.N;
        }

        public void ProcessFunctionOverData(Action<int, int> func)
        {
            for (var i = 0; i < this.M; i++)
            {
                for (var j = 0; j < this.N; j++)
                {
                    func(i, j);
                }
            }
        }

        public static Matrix CreateIdentityMatrix(int n)
        {
            var result = new Matrix(n, n);
            for (var i = 0; i < n; i++)
            {
                result[i, i] = 1;
            }

            return result;
        }

        public Matrix CreateTransposeMatrix()
        {
            var result = new Matrix(this.N, this.M);
            result.ProcessFunctionOverData((i, j) => result[i, j] = this[j, i]);
            return result;
        }

        public Matrix(int m, int n)
        {
            this.m = m;
            this.n = n;
            this.data = new double[m, n];
            this.ProcessFunctionOverData((i, j) => this.data[i, j] = 0);
        }

        public double this[int x, int y]
        {
            get { return this.data[x, y]; }
            set
            {
                this.data[x, y] = value;
                this.precalculatedDeterminant = double.NaN;
            }
        }

        public double CalculateDeterminant()
        {
            if (!double.IsNaN(this.precalculatedDeterminant))
            {
                return this.precalculatedDeterminant;
            }

            if (!this.IsSquare)
            {
                throw new InvalidOperationException("determinant can be calculated only for square matrix");
            }

            if (this.N == 2)
            {
                return this[0, 0] * this[1, 1] - this[0, 1] * this[1, 0];
            }

            double result = 0;
            for (var j = 0; j < this.N; j++)
            {
                result += (j % 2 == 1 ? 1 : -1) * this[1, j] *
                          this.CreateMatrixWithoutColumn(j).CreateMatrixWithoutRow(1).CalculateDeterminant();
            }

            this.precalculatedDeterminant = result;
            return result;
        }

        public Matrix CreateInvertibleMatrix()
        {
            if (this.M != this.N)
                return null;
            var determinant = CalculateDeterminant();
            if (Math.Abs(determinant) < Constants.DoubleComparisonDelta)
                return null;

            var result = new Matrix(M, M);
            ProcessFunctionOverData((i, j) =>
            {
                result[i, j] = ((i + j) % 2 == 1 ? -1 : 1) * CalculateMinor(i, j) / determinant;
            });

            result = result.CreateTransposeMatrix();
            return result;
        }

        private double CalculateMinor(int i, int j)
        {
            return CreateMatrixWithoutColumn(j).CreateMatrixWithoutRow(i).CalculateDeterminant();
        }

        private Matrix CreateMatrixWithoutRow(int row)
        {
            if (row < 0 || row >= this.M)
            {
                throw new ArgumentException("invalid row index");
            }

            var result = new Matrix(this.M - 1, this.N);
            result.ProcessFunctionOverData((i, j) => result[i, j] = i < row ? this[i, j] : this[i + 1, j]);
            return result;
        }

        private Matrix CreateMatrixWithoutColumn(int column)
        {
            if (column < 0 || column >= this.N)
            {
                throw new ArgumentException("invalid column index");
            }

            var result = new Matrix(this.M, this.N - 1);
            result.ProcessFunctionOverData((i, j) => result[i, j] = j < column ? this[i, j] : this[i, j + 1]);
            return result;
        }

        public static Matrix LUMatrix(Matrix matrix)
        {
            for (int k = 0; k < matrix.n - 1; k++)
            {
                for (int i = k + 1; i < matrix.n; i++)
                    matrix[k, i] = matrix[k, i] / matrix[k, k];
                for (int j = k + 1; j < matrix.n; j++)
                {
                    for (int i = k + 1; i < matrix.n; i++)
                        matrix[i, j] = matrix[i, j] - (matrix[i, k] * matrix[k, j]);
                }
            }

            return matrix;
        }

        public static Matrix operator *(Matrix matrix, double value)
        {
            var result = new Matrix(matrix.M, matrix.N);
            result.ProcessFunctionOverData((i, j) => result[i, j] = matrix[i, j] * value);
            return result;
        }

        public static Matrix operator *(Matrix matrix, Matrix matrix2)
        {
            if (matrix.N != matrix2.M)
            {
                throw new ArgumentException("matrixes can not be multiplied");
            }

            var result = new Matrix(matrix.M, matrix2.N);
            result.ProcessFunctionOverData((i, j) =>
            {
                for (var k = 0; k < matrix.N; k++)
                {
                    result[i, j] += matrix[i, k] * matrix2[k, j];
                }
            });
            return result;
        }

        public static Matrix operator +(Matrix matrix, Matrix matrix2)
        {
            if (matrix.M != matrix2.M || matrix.N != matrix2.N)
            {
                throw new ArgumentException("matrixes dimensions should be equal");
            }

            var result = new Matrix(matrix.M, matrix.N);
            result.ProcessFunctionOverData((i, j) => result[i, j] = matrix[i, j] + matrix2[i, j]);
            return result;
        }

        public static Matrix operator -(Matrix matrix, Matrix matrix2)
        {
            return matrix + (matrix2 * -1);
        }

        public static double Det(Matrix matrix)
        {
            double det = 1.0;
            for (int i = 0; i < matrix.n; i++)
                det = det * matrix[i, i];
            return det;
        }

        public static Matrix GetL(Matrix m)
        {
            for (int i = 0; i < m.data.GetLength(0); i++)
                m[i, i + 1] = 0;
            return m;
        }
        public static Matrix GetU(Matrix m)
        {
            for (int i = 0; i < m.data.GetLength(0); i++)
                m[i, i + 1] = 0;
            return m;
        }
        // def get_L(m):
        // L = m.copy()
        // for i in range(L.shape[0]):
        // L[i, i + 1:] = 0
        // print("Матриця L:")
        // print(L)
        //     return L
        //
        //
        //     def get_U(m):
        //     U = m.copy()
        // for i in range(U.shape[0]):
        // U[i, :i] = 0
        // U[i, i] = 1
        // print("Матриця U:")
        // print(U)
        //     return U

        public static void ShowMatrix(Matrix matrix)
        {
            for (int i = 0; i < matrix.n; i++) {
                for (int j = 0; j < matrix.n; j++) {
                    Console.Write(matrix[i,j] + ", ");    
                }
                Console.WriteLine();
            }
        }
    }
        
        
        //def inverse(LU):
        //     l_inv = np.linalg.inv(get_L(LU))
        // u_inv = np.linalg.inv(get_U(LU))
        // A_inv = np.dot(u_inv, l_inv)
        //     print("Обернена матриця:")
        // print(A_inv)
//------------------------
        //     def solve_LU(lu_matrix, b):
        //     y = np.matrix(np.zeros([lu_matrix.shape[0], 1]))
        // for i in range(y.shape[0]):
        // y[i, 0] = (b[i, 0] - lu_matrix[i, :i] * y[:i]) / lu_matrix[i, i]
        // x = np.matrix(np.zeros([lu_matrix.shape[0], 1]))
        // for i in range(1, x.shape[0] + 1):
        // x[-i, 0] = (y[-i] - lu_matrix[-i, -i:] * x[-i:, 0])
        // return x
        //
        //
        //     def get_L(m):
        //     L = m.copy()
        // for i in range(L.shape[0]):
        // L[i, i + 1:] = 0
        // print("Матриця L:")
        // print(L)
        //     return L
        //
        //
        //     def get_U(m):
        //     U = m.copy()
        // for i in range(U.shape[0]):
        // U[i, :i] = 0
        // U[i, i] = 1
        // print("Матриця U:")
        // print(U)
        //     return U
        //
        //
        //     def inverse(LU):
        //     l_inv = np.linalg.inv(get_L(LU))
        // u_inv = np.linalg.inv(get_U(LU))
        // A_inv = np.dot(u_inv, l_inv)
        //     print("Обернена матриця:")
        // print(A_inv)
    }
