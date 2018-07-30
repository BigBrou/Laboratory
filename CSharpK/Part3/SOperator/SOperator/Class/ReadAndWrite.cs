using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SOperator
{
    class ReadAndWrite
    {
        private static string FStr;

        public static string ReadInConsole()
        {
            FStr = System.Console.ReadLine();

            return FStr;
        }

        public static void WriteInConsole(string MStr)
        {
            System.Console.WriteLine(MStr);
        }
    }
}
