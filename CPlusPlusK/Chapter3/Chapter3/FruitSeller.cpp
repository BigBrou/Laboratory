#include "stdafx.h"
#include "FruitSeller.h"
#include <iostream>

using namespace std;


void FruitSeller::InitMembers(int price, int num, int money)
{
	APPLE_PRICE = price;
	numOfApples = num;
}

int FruitSeller::SaleApples(int money)
{
	int num = money / APPLE_PRICE;
	numOfApples -= num;
	myMoney += money;
	
	return num;
}
void FruitSeller::ShowSaleResult()
{
	cout << "Num of Apples " << numOfApples << endl;
	cout << "Margin " << APPLE_PRICE << endl;
}
