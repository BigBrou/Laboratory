#include "stdafx.h"
#include "FruitBuyer.h"
#include "FruitSeller.h"
#include <iostream>

using namespace std;

void FruitBuyer::InitMembers(int money)
{
	myMoney = money;
	numOfApples = 0;
}

void FruitBuyer::BuyApples(FruitSeller &Seller, int money)
{
	numOfApples += Seller.SaleApples(money);
	myMoney -= money;
}

void FruitBuyer::ShowBuyResult()
{
	cout << "Money Left " << myMoney << endl;
	cout << "Apple Bought " << numOfApples << endl;
}