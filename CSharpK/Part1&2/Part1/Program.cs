using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Part1
{
    class Program
    {
        static void Main(string[] args)
        {
            string ResultStr = string.Empty;

            /* Part1 Test
            Class1 ClassTest = new Class1();
            ClassTest.ReadAndWrite();
            */

            /*
            Class2 ClassTest2 = new Class2();
            string Class2InputStr = string.Empty;
            int ResultPosInt = -1;

            Class2InputStr = "Class2InputStr";
            ResultStr = ClassTest2.stringStaticMethod(Class2InputStr, ResultPosInt);
            ResultStr = ClassTest2.stringMethod(ResultStr);
            */

            /*
            Class3 Class3Test = new Class3();
            ResultStr = Class3Test.CastTry();
            */

            Class4 Class4Test = new Class4();
            int[][] Array = new int[0][];
            ResultStr = Class4Test.initalizeCells().ToString();
            //showResultStr(ResultStr);
            ResultStr = Class4Test.AllocVariableCells(Array).ToString();
            //showResultStr(ResultStr);
            Class4Test.ArrayFunction();

            //showResultStr(ResultStr);
        }

        public static void showResultStr(string iInputString)
        {
            System.Console.WriteLine(iInputString);
            System.Console.ReadLine();
        }
    }
}
