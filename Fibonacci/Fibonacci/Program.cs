using System;
using System.Collections.Generic;

namespace Fibonacci
{
    static class Program
    {

        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number to find out the fibonacci sum...");
            int number = Convert.ToInt32(Console.ReadLine());

            Dictionary<int, int> dict = new Dictionary<int, int>();

            //int res = Fib(number);
            //int res = Fib_recursive(number);
            Func<int, int> fibonacci = Fib_recursive;
            var fibonacciMemoized = fibonacci.Memoize();
            int res = fibonacciMemoized(number);

            Console.WriteLine(res);

        }

        /*
         * A simple iterative solution.
         */
        static int Fib(int n)
        {
            int F1 = 1;
            int F2 = 1;

            int result = 1;
            for (int i = 2; i < n; i++)
            {
                result = F1 + F2;
                F1 = F2;
                F2 = result;
            }
            return result;
        }

        /*
         * A naive recursive solution. This has very bad performance since we recalculate alot of fibonacci numbers in our recursive
         * branch tree.
         */
        static int Fib_recursive(int n)
        { 
            return n <= 2 ? 1 : Fib_recursive(n - 1) + Fib_recursive(n - 2);
        }

        /*
         * A generic memoize function that takes a function as its input, checks whether the item is in the cache and if not, adds it to the cache.
         * This allows us to memoize the function correctly.
         */
        public static Func<T, TResult> Memoize<T, TResult>(this Func<T, TResult> func)
        {

            var dict = new Dictionary<T, TResult>();

            // Return a lambda function. We can pass our fibonacci as an argument to this function and then update our
            // dictionary cache in order to memoize partial results.
            return n =>

            {

                if (dict.ContainsKey(n)) return dict[n];

                var result = func(n);

                dict.Add(n, result);

                return result;

            };

        }
    }
}
