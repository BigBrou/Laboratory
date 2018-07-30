#ifndef __FRUITBUYER_H__
#define __FRUITBUYER_H__
#include "FruitSeller.h"

class FruitBuyer
{
public:
	void InitMembers(int money);
	void BuyApples(FruitSeller &Seller, int money);
	void ShowBuyResult();
private:
	int myMoney;
	int numOfApples;
};

#endif 

