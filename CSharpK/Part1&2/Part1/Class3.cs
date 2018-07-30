using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Part1
{
    class Class3
    {
        private long longNumber;
        private int intNumber;
        private float floatNumber;
        private double doubleNumber;

        private string str;

        private bool boolValue;

        public Class3()
        {
            this.longNumber = 123456789;
            this.str = string.Empty;
        }

        public void CastLongToInt()
        {
            //explicit casting 
            intNumber = (int)longNumber;
        }

        public void CastIntToLong()
        {
            //implicit Casting
            this.intNumber = 12345;
            this.longNumber = this.intNumber;
        }

        public float CastStrToFloat()
        {
            //use parse
            this.str = "9.11E-31";
            this.floatNumber = float.Parse(str);

            return this.floatNumber;
        }

        public double CastStrToDouble()
        {
            this.str = "214.5645";
            this.doubleNumber = System.Convert.ToDouble(str);
            this.boolValue = System.Convert.ToBoolean(str);

            return doubleNumber;
        }

        public string ReturnValueByString()
        {
            this.doubleNumber = 1234.5234;
            //Convert.ToString(doubleNumber);
            //모든 값 변수는 ToString 으로 나타낼 수 있다

            return doubleNumber.ToString();
        }

        public string CastTry()
        {
            this.intNumber = 12345;
            this.str = "1234EE";

            if (double.TryParse(str, out doubleNumber))
            {
                str = "TryParse Well Done : ";
                str = string.Concat(str, doubleNumber.ToString());
            }
            else
            {
                str = "TryParse not occured : " + str;
            }

            return str;
        }

        public int UseCheck(int AValue)
        {
            checked
            { 
                // throws OverflowException at the runtime
                // unchecked 사용할 경우에는 -~~~ 값으로 나오고, 일반적으로 나옴
                AValue = int.MaxValue;
                AValue += 1;

                return AValue;
            }
        }

    }
}
