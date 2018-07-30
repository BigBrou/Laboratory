using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Net;

namespace MethodAndParameter
{
    class Program
    {
        static int Main(string[] args)
        {
            int result;
            string targetFileName;
            string url;

            switch (args.Length)
            {
                default:
                    Console.WriteLine("ERROR: You Muist Specify the URL and the file name");
                    targetFileName = null;
                    url = null;
                    break;

                case 2:
                    url = args[0];
                    targetFileName = args[1];
                    break;
            }

            if((targetFileName != null) && (url != null))
            {
                WebClient webClient = new WebClient();
                webClient.DownloadFile(url, targetFileName);
                result = 0;
            }
            else
            {
                Console.WriteLine("Usage: Downloader.exe <URL><TargetFileName>");
                result = 1;
            }

            return result;
        }

        public static void DoMethodDeclaration(string iFirstName, string iLastName)
        {
            //string FirstName = string.Empty;
            //string LastName = string.Empty;

            //DoMethodDeclaration(FirstName, LastName);


            MethodDeclaration MD = new MethodDeclaration();
            iFirstName = MD.GetUserInput();
            iLastName = MD.GetUserInput();

            System.Console.WriteLine(MD.GetFullName(iFirstName, iLastName));
        }
    }
}
