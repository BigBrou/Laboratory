using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SOperator.Operators;

namespace SOperator
{
    class Program
    {
        static void Main(string[] args)
        {
            Ex3_45_Test();

            // Do Not Erase;
            System.Console.ReadLine();
        }

        public static void Assert()
        {
            AssertTest Assert = new AssertTest();
            Assert.Assert();
        }

        public static void Ex3_43_Test()
        {
            Ex3_43 Ex3_43_Obj = new Ex3_43();

            Ex3_43_Obj.UseInput();

        }

        public static void Ex3_45_Test()
        {
            Ex3_45 Ex3_45_Obj = new Ex3_45();

            Ex3_45_Obj.BinaryConvert();
        }
    }
}
