using System;
using System.Text;
using System.Linq;
using System.IO;

namespace csCoreTest
{
    class Program
    {
        static void Main(string[] args)
        {
           string source = "Hello World!";
           string result = new string(source.Select(n => n == ' ' ? '\t' : n).ToArray());

            File.WriteAllText("tmpFile",new string(File.ReadAllText("testfile").Select(n => n == ' ' ? '\t' : n).ToArray()),Encoding.UTF8);
           
            Console.WriteLine(result);
        }
    }
}
