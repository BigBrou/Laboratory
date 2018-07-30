using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SOperator.Operators
{
    class Ex3_45
    {
        private const int size = 64;
        private ulong value;
        private char bit;

        public void BinaryConvert()
        {
            System.Console.WriteLine("Insert Number : ");
            value = (ulong)long.Parse(System.Console.ReadLine());

            ulong mask = 1UL;

           


            //ulong mask = 1UL << size - 1;
            for (int AIdx = 0; AIdx < size-1; AIdx ++)
            {
                mask = mask << 1;
                System.Console.WriteLine(Convert.ToInt64(mask));

                //bit = ((mask & value) > 0 ? '1' : '0');
                //System.Console.Write(bit);

                //mask >>= 1;
            }
        }
    }
}
