using System;
using System.IO;
using System.Text;
using System.Linq;


namespace csCoreTest
{
    public class Core : IChanger
    {

        private static Core instance;

        public Core()
        {            
        }

        public static Core GetInstance()
        {
            if (Core.instance == null)
                instance =  new Core();
            
            return instance;
        }


        public void ChangeChar(string file, char whatChange, char newValue) => Change(file, whatChange, newValue);


        private void Change(string file, char whatChange, char newValue)
        {
            File.WriteAllText(file, new string(File.ReadAllText(file).Select(n => n == whatChange ? newValue : n).ToArray()), Encoding.UTF8);

        }

  

    }
}