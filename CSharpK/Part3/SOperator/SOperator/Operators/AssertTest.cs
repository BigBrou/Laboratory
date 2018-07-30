using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace SOperator
{
    class AssertTest
    {
        private float floatNumber;
        private double doubleNumber;
        private decimal decimalNumber;

        public void Assert()
        {
            floatNumber = 0.1F * 42F;
            decimalNumber = 4.2M;

            Trace.Assert((decimal)floatNumber != decimalNumber);
        }
    }
}
