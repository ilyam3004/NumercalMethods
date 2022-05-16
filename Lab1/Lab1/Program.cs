using System;

namespace Lab1
{
    class Program
    {
        public static void Main(string[] args)
        {
            /*/*----Функція f(x)(метод хорд)(1;1,5)(-1;-1,5)(1,5;1,8)(4,3;4,7)---*/
            for (int i = 0; i < 4; i++){                                               
                
                Console.WriteLine("Function f(x)(chord method)");                       
                Console.WriteLine("Enter 1st interval:");
                double fInterv = double.Parse(Console.ReadLine()); //перший інтервал
                Console.WriteLine("Enter 2nd interval:");
                double sInterv = double.Parse(Console.ReadLine()); //другий інтервал
                Console.WriteLine("Enter accuracy:");
                double precision = double.Parse(Console.ReadLine()); //точність
                Console.WriteLine("x" + (i+1) + " = " + MethodChord(FunctionF, fInterv, sInterv, precision));
                Console.WriteLine("-----------------------\n");
            }
            /*-------------- Функція f(x)(метод бісекції) ---------------*/
            for (int i = 0; i < 4; i++)
            {
                Console.WriteLine("Function f(x)(bissection method)");
                Console.WriteLine("Enter 1st interval:");
                double fInterv2 = double.Parse(Console.ReadLine()); //перший інтервал
                Console.WriteLine("Enter 2nd interval:");
                double sInterv2 = double.Parse(Console.ReadLine()); //другий інтервал
                Console.WriteLine("Enter accuracy:");
                double precision2 = double.Parse(Console.ReadLine()); //точність
                Console.WriteLine("x" + (i+1) + " = " + BissectionMethod(FunctionF, fInterv2, sInterv2, precision2));
                Console.WriteLine("-----------------------\n");
            }
            /*-------------- Функція g(x)(метод хорд) ---------------*/
            for (int i = 0; i < 2; i++) {
                Console.WriteLine("Function g(x)(chord method):");
                Console.WriteLine("Enter 1st interval:");
                double fInterv3 = double.Parse(Console.ReadLine()); //перший інтервал
                Console.WriteLine("Enter 2nd interval:");
                double sInterv3 = double.Parse(Console.ReadLine()); //другий інтервал
                Console.WriteLine("Enter accuracy:");
                double precision3 = double.Parse(Console.ReadLine()); //точність
                Console.WriteLine("x" + (i+1) + " = " + MethodChord(FunctionG, fInterv3, sInterv3, precision3));
                Console.WriteLine("-----------------------\n");
            }
        }
        public static double FunctionF(double x) //функція f(x)
        {
            return 35 * Math.Pow(Math.Cos(x), 2) - 2 * Math.Cos(x) - 1;
        }
        public static double FunctionG(double x) // функція g(x)
        {
            return 25 * Math.Pow(Math.Cos(x), 2) - 10 * Math.Cos(x) + 1;
        }
        
        public static double MethodChord(Func <double, double> f, double FInterv, double SInterv, double precision)
        {
            double result = 0.0;
            double temp;
            do
            {
                temp = result;
                result = SInterv - f(SInterv) * (FInterv - SInterv) / (f(FInterv) - f(SInterv));//знаходимо точку перетину графіка функції з віссю х
                /*Переоприділяємо границі інтервалу*/
                FInterv = SInterv;
                SInterv = temp;
            }
            while (Math.Abs(result - SInterv) > precision);//перевірка умови наближеності точки перетину графіка функції до кореня рівняння
            return result;
        }
        public static double BissectionMethod(Func<double, double> f,double FInterv, double SInterv, double precision)
        {
            double result;
            while (true)
            {
                result = (FInterv + SInterv) / 2; //середина інтервалу
                if (f(result) == 0.0 || Math.Abs(f(result)) < precision)//перевірка, чи не є середина інтервалу коренем рівняння
                    return result;
                if (f(FInterv) * f(result) < 0)//перевірка, чи корінь знаходиться зліва
                    SInterv = result;
                else if (f(SInterv) * f(result) < 0)//перевірка, чи корінь знаходиться справа
                    FInterv = result; 
            }
        }
    }
}