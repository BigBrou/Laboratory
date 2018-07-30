#ifndef __FRUITSELLER_H__
#define __FRUITSELLER_H__

class FruitSeller
{
public:
	void InitMembers(int price, int num, int money);
	int SaleApples(int money);
	void ShowSaleResult();
private:
	int APPLE_PRICE;
	int numOfApples;
	int myMoney;
};

#endif