#include "stdafx.h"
#include "FruitBuyer.h"
#include "FruitSeller.h"
#include <iostream>

using namespace std;

int main(void)
{
	FruitSeller seller;
	seller.InitMembers(1000, 20, 0);
	
	FruitBuyer buyer;
	buyer.InitMembers(5000);
	buyer.BuyApples(seller, 2000);

	seller.ShowSaleResult();
	buyer.ShowBuyResult();

	int num;
	cin >> num;

	return 0;
}