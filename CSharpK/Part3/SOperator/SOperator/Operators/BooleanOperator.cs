using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SOperator.Operators
{
    class BooleanOperator
    {
        private bool DefaultBool = false;

        /// <summary>
        /// 관계 연산자 
        /// </summary>
        public bool IsSmall(int x, int y) { return x < y; }
        public bool IsLarge(int x, int y) { return x > y; }
        public bool IsSame(int x, int y) { return x == y; }
        public bool IsNotSame(int x, int y) { return x != y; }

        /// <summary>
        /// 논리 부울 연산자 
        /// </summary>
        public bool orOperator(bool x, bool y) { return x || y; }
        public bool andOperator(bool x, bool y) { return x && y; }
        public bool xorOperator(bool x, bool y) { return x ^ y; }
        public bool notOperator(bool x) { return !x; }

        /// <summary>
        /// 조건 연산자 
        /// </summary>
        public bool conditionOperator(bool x)
        {
            return (x == true) ? true : false;
        }

        public string NullOperator(string x)
        {
            return x ?? "DefaultX";
        }

        public string NullOperator2(string x)
        {
            if (x?.ToLower().StartsWith("string") ?? false)
            {
                x = "string is Exist";
            }
            else
            {
                x = "string is Null";
            }

            return x; 
        }
    }
}
