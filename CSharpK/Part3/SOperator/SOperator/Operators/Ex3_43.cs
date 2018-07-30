using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SOperator.Operators
{
    class Ex3_43
    {
        private decimal current;
        private decimal previous;
        private decimal temp;
        private decimal input;

        public void UseInput()
        {
            this.input = decimal.Parse(System.Console.ReadLine());

            current = previous = 1;

            while (current < input)
            {
                temp = current;
                current = previous + current;
                previous = temp;
            }

            System.Console.WriteLine($"The Fibonacci number following this is  {current}");
        }
        
    }
}
