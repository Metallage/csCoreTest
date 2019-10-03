using System;
using System.Collections.Generic;
using System.Text;

namespace csCoreTest
{
    public interface IChanger
    {
        public void ChangeChar(string file, char whatChange, char newValue);
    }
}
