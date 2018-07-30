using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Part1
{
    class Class2
    {
        // Variables
        // 기본 숫자 형식 
        // 정수형식, 부동소수점 형식, 표현오류없이 큰 수 저장하는 Decimal 3단계 구성

        //정수형식
        private sbyte sbyteType;
        private byte byteType;

        private short shortType;
        private ushort ushortType;

        private int intType;
        private uint uintType;

        private long longType;
        private ulong ulongType;

        //부동소수점
        private float floatType;
        private double doubleType;

        //Decimal
        private decimal decimalType;


        // 문자열
        private char charType;
        private string stringType;

        public Class2() {}

        public decimal ReturnDecimal()
        {
            this.decimalType = 1.12345678901234567890M; // m, M 으로 명시적 선언

            return this.decimalType;
        }

        public string stringStaticMethod(string iString, int iPosition)
        {
            this.stringType = string.Empty;
            this.stringType = "stringType";

            iString = string.Format("Test Print of Format using {0} : ", this.stringType);
            iString = string.Concat(iString, stringType);
            iPosition = string.Compare(this.stringType, iString);

            return iString;
        }

        public string stringMethod(string iString)
        {
            this.stringType = string.Empty;
            this.stringType = iString.ToLower();
            this.stringType = iString.Replace("using", "usingBy");

            return this.stringType;
        }
    }
}
