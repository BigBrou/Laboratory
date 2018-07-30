using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Part1
{
    /// <summary>
    /// this Class talks about Array
    /// </summary>

    class Class4
    {
        //Declaration
        string[] ComputerLanguages;
        int[,] Cells;
        int[][] VaiableCells;
        int Count = default(int);

        public Class4()
        {
            // Allocation
            ComputerLanguages = new string[5];
            Cells = new int[2, 3];

            // Initialization
            ComputerLanguages = new string[]{
                "Delphi", "C#", "JAVA", "C++", "Python" 
            };
        }

        public int initalizeCells()
        {
            this.Cells = new int[,]{
                {1, 2, 3},
                {2, 3, 4}
            };

            return Cells[1, 0];
        }

        public int AllocVariableCells(int [][] ACells)
        {
            ACells = new int [][]{
                new int[] {1, 2, 3, 4 },
                new int[] {8, 2, 3},
                new int[] {1}
            };
            ACells[0] = new int []{ 2, 3, 4, 5};
            this.VaiableCells = ACells;

            return ACells[1][0];
        }

        public void ArrayFunction()
        {
            string ALanguageFind = string.Empty;
            int AIdx = default(int);

            ALanguageFind = "JAVA";

            System.Array.Sort(ComputerLanguages);
            Count = System.Array.BinarySearch(ComputerLanguages, ALanguageFind);
            System.Console.WriteLine("Array Sort");
            System.Console.WriteLine(Count);

            System.Array.Reverse(ComputerLanguages);
            Count = System.Array.BinarySearch(ComputerLanguages, ALanguageFind);
            if (Count >= 0)
            { 
                System.Console.WriteLine("Array Reverse");
                System.Console.WriteLine(Count);
            }

            System.Array.Clear(ComputerLanguages, 0, 1);
            for (AIdx = 0; AIdx < ComputerLanguages.Length; AIdx++)
                System.Console.WriteLine(string.Concat(AIdx.ToString()+" : ",  ComputerLanguages[AIdx]));

            Console.WriteLine(Cells.GetLength(1));

            System.Console.ReadLine();
        }
    }
}
