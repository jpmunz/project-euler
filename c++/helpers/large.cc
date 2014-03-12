#include "large.h"

ostream& operator<<(ostream& output, const LargeNumber& n) {
	for(int i = n.digits() - 1; i >= 0; i--)
		output << n.get_digit(i);
    return output;
}

LargeNumber::LargeNumber(int n) 
{
	if(n==0)
	{
		number.push_back(0);
	}
	else
	{
		while(n > 0)
		{
			number.push_back(n % 10);
			n /= 10;
		}
	}
}

int LargeNumber::get_digit(int i) const
{
	return number[i];
}
int LargeNumber::digits() const
{
	return number.size();
}

LargeNumber & LargeNumber::operator+=(const LargeNumber &rhs)
{
	for(int i = 0; i < rhs.number.size(); i++)
	{
		if(i == this->number.size())
				this->number.push_back(0);

		this->number.at(i) += rhs.number[i];

		int j = i;
		while(this->number.at(j) > 9)
		{
			this->number.at(i) %= 10;

			if(j == this->number.size() - 1)
				this->number.push_back(1);
			else
				this->number.at(i+1) ++;
		}
	}

	return *this;
}

const LargeNumber LargeNumber::operator+(const LargeNumber &other) const 
{
	LargeNumber result = *this;
	result += other;
	return result;
}
