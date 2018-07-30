#include "stdafx.h"

/*
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

namespace CAR_CONST
{
	enum
	{
		ID_LEN = 20,
		MAX_SPD = 200,
		FUEL_STEP = 2,
		ACC_STEP = 10,
		BRK_STEP = 10
	};
}

class Car
{
public:
	void InitMembers(string ID, int fuel);
	void ShowCarState();
	void Accel();
	void Break();

private:
	string gamerID;
	int fuelGauge;
	int curSpeed;
};

void Car::InitMembers(string ID, int fuel)
{
	gamerID = ID;
	fuelGauge = fuel;
}

void Car::ShowCarState()
{
	cout << "ID" << gamerID << endl;
	cout << "Fuel" << fuelGauge << endl;
	cout << "Speed" << curSpeed << endl;
}
void Car::Accel() 
{
	if (fuelGauge <= 0)
		return;
	else
		fuelGauge -= CAR_CONST::FUEL_STEP;

	if (curSpeed + CAR_CONST::ACC_STEP >= CAR_CONST::MAX_SPD)
	{
		curSpeed = CAR_CONST::MAX_SPD;
		return;
	}

	curSpeed += CAR_CONST::ACC_STEP;
}
void Car::Break() 
{
	if (curSpeed < CAR_CONST::BRK_STEP)
	{
		curSpeed = 0;
		return;
	}

	curSpeed -= CAR_CONST::BRK_STEP;
}

int main(void)
{
	Car run99;
	run99.InitMembers("run99", 100);
	run99.Accel();
	run99.Accel();
	run99.Accel();
	run99.ShowCarState();
	
	return 0;
}
*/