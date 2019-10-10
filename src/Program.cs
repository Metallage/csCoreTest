using System;


namespace csCoreTest
{
    class Program
    {
        static int Main(string[] args)
        {
            if(args.Length == 0)
            {
                Console.WriteLine("Enter path to file...");
                return 1;
            }

            string fileName = args[0];
            char whatToChange = ' ';
            char newValue = '\t';

            Core changer = Core.GetInstance();
            changer.ChangeChar(fileName, whatToChange, newValue);
            return 0;
        }
    }
}
