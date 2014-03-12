#include <iostream>
#include <vector>

using namespace std;

class LargeNumber
{
	friend ostream& operator<<(ostream& output, const LargeNumber& n);
public:
	LargeNumber(int n);
	LargeNumber & operator+=(const LargeNumber &rhs);
	const LargeNumber operator+(const LargeNumber &other) const;
	int digits() const;
	int get_digit(int i) const;
private:
	vector<int> number;

};
