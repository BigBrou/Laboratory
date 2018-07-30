using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MethodAndParameter
{
    class MethodDeclaration
    {        
        public string GetUserInput()
        {
            System.Console.WriteLine("Write Name");

            return System.Console.ReadLine();
        }

        public string GetFullName(string iFirstName, string iLastName)
            => $"{iFirstName}{iLastName}";

        public string GetInitials(string iFirstName, string iLastName)
        {
            return $"{iFirstName[0]}, {iLastName[0]}";
        }

    }
}
