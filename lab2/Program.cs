using System;
using System.Numerics;

namespace lab2
{
    class Program
    {
        public static void Main(string[] args)
        {
            //Task 2(Function f(x) and g(x))
            double e = 0.0001;
            Console.WriteLine("Newton method(function f(x)):");
            Console.WriteLine($"x1 = {NewthonMethodF(new Complex(0,0),e)}");
            Console.WriteLine("Newton Method(function g(x)):");
            Console.WriteLine($"x1 = {NewthonMethodG(new Complex(0.5,0), e)}");
            Console.WriteLine($"x2 = {NewthonMethodG(new Complex(-1,2),e)}");
            Console.WriteLine($"x3 = {NewthonMethodG(new Complex(-1,-2), e)}");
            Console.WriteLine("Simple Newton method(function f(x)):");
            double e1 = 0.00001;
            double e2 = 0.01;
            Console.WriteLine($"x1 = {NewthonMethodF(new Complex(0,0), e2)}");
            Console.WriteLine("Simple Newton method(function g(x)):");
            Console.WriteLine($"x1 = {SimpleNewthonMethodG(new Complex(0.5,0), e1)}");
            Console.WriteLine($"x2 = {SimpleNewthonMethodG(new Complex(-1,2),e1)}");
            Console.WriteLine($"x3 = {SimpleNewthonMethodG(new Complex(-1,-2), e1)}");
            //Task4(Function k(x) and l(x))
            Console.WriteLine("Itheration method(function p(x)):");
            ItherationMethod.K(new Complex(0,0), e1);
            Console.WriteLine("Itheration method(function q(x)):");
            Console.WriteLine($"x1 = {ItheratinMethod(new Complex(-1,0), e1)}");
            Console.WriteLine($"x2 = {ItheratinMethod(new Complex(-1,2), e1)}");
            Console.WriteLine($"x3 = {ItheratinMethod(new Complex(-1,-2), e1)}");
        }
        //------------ Function F ------------
        static Complex f(Complex x)
        {
            return (Complex.Tan(0.47 * x + 0.2) - (x*x));
        }

        static Complex DifF(Complex x)
        {
            Complex temp = Complex.Tan((47.0 * x + 20.0)/100.0);
            Complex temp1 = 47.0 * Complex.Pow(temp, 2) + 47.0;
            return (temp1/100.0) - (2 * x);
        }
        //------------ Function G ------------
        static Complex g(Complex x)
        {
            return (x*x*x) + 2 * (x*x) + x - 1;
        }
        static Complex DifG(Complex x)
        {
            return (3 * (x * x) + (4 * x) + 1);
        }
        static Complex GChange(Complex x)
        {
            return -(x*x*x)- 2 * (x*x)+ 1;
        }
        static Complex DifGChange(Complex x)
        {
            return -3*(x*x)-4*x;
        }
        //--------------Function K-------------------
        static Complex k(Complex x)
        {
            Complex temp = Complex.Log10(x + 2.0);
            return Complex.Pow(temp, 1.0/2.0);
        }
        static Complex DifK(Complex x)
        {
            Complex temp1 = Complex.Pow(Complex.Log(10), 1.0/2.0);
            Complex temp2 = (2 * x + 4) * Complex.Log(10) * Complex.Pow(Complex.Log(x + 2), 1.0 / 2.0);
            return temp1/temp2;
        }
        static Complex KChange(Complex x)
        {
            return -(x*x*x)- 2 * (x*x)+ 1;
        }
        static Complex DifKChange(Complex x)
        {
            return -3*(x*x)-4*x;
        }
        //--------------Function L-------------
        static Complex l(Complex x)
        {
            return (x*x*x)+3*(x*x)+(6*x)-1;
        }
        static Complex DifL(Complex x)
        {
            return 3*(x*x) + 6*x + 6;
        }
        static Complex LChange(Complex x)
        {
            return (-(x*x*x)-3*(x*x)+1)/6.0;
        }
        static Complex DifLChange(Complex x)
        {
            return (-(x*x)/2)-x;
        }
        static Complex NewthonMethodF(Complex z, double e)
        {
            Complex d = new(1,0); 
            while (Math.Abs(d.Real) > e) { 
                    d = f(z)/DifF(z);
                    z = z - d; 
            }
            return z;
        }
        static Complex NewthonMethodG(Complex z, double e)
        {
            Complex d = new(1,0); 
            while (Math.Abs(d.Real) > e) { 
                d = g(z)/DifG(z);
                z = z - d; 
            }
            return z;
        } 
        static Complex SimpleNewthonMethodF(Complex z, double e)
        {
            Complex d = new(1,0);
            Complex diff = DifF(z);
            while (Math.Abs(d.Real) > e) {
                d = f(z)/diff;
                z = z - d;
            }
            return z;
        }
        static Complex SimpleNewthonMethodG(Complex z, double e)
        {
            Complex d = new(-1,0);
            Complex diff = DifG(z);
            while (Math.Abs(d.Real) > e) {
                d = g(z)/diff;
                z = z - d;
            }
            return z;
        }
        static Complex ItheratinMethod(Complex z, double e)
        {
            if(DifLChange(z).Real < 1)
            {
                Complex d = new (1,0);
                while(Math.Abs(d.Real) > e){
                    d = z - LChange(z);
                    z = LChange(z); 
                }
            }
            else
            {
                Complex d = new(1,0);
                Complex diff = -11.5;
                while (Math.Abs(d.Real) > e) {
                    d = l(z)/diff;
                    z = z - d;
                }
                return z;
            }
            return z;
        }
    }
}