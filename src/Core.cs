using System;
using System.IO;
using System.Text;
using System.Linq;


namespace csCoreTest
{
    public class Core
    {
        private void ChangeTab(string fileName)
        {
            
            using (FileStream fs = File.OpenWrite(fileName))
            {
                byte[] b = new byte[1024];
                UTF8Encoding temp = new UTF8Encoding(true);
                while (fs.Read(b,0,b.Length) > 0)
                {
                    string tmpString=temp.GetString(b);
                }
            }
            

        }

        private string FindTab(string tmpString)
        {

            return new string(tmpString.Select(n => n == ' ' ? '\t' : n).ToArray());
        }


    }
}