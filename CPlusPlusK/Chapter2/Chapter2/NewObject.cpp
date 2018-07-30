#include "stdafx.h"
#include <iostream>
#include <string.h>

using namespace std;

class Simple
{
	public:
		Simple()
		{
			cout << "I'm Simple Constructor " << endl;
		}
};

int main(void)
{
	Simple *sp1 = new Simple;
	Simple *sp2 = (Simple*)malloc(sizeof(Simple) * 1);

	delete sp1;
	free(sp2);

	int num1;
	cin >> num1;

	return 0;
}