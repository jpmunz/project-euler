#include <iostream>
#include <time.h>
#include <memory.h>

using namespace std;

int main()
{
	//Start from September 1, 1901 (The first Sunday on the first of a month in the twentieth century)
	int year = 1;
	int sundays = 1;
	int month = 8;
	int days_since_sunday = 0;

	int days_in_month[] = {31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

	for(;;)
	{
		int days_to_add;

		if(month == 1)
			days_to_add = (year % 4 == 0) ? 29 : 28;
		else
			days_to_add = days_in_month[month];

		days_since_sunday += days_to_add;

		if(days_since_sunday % 7 == 0)
			sundays++;

		month++;

		if(month > 11)
		{
			month = 0;
			year++;

			if(year > 100)
				break;
		}

	}

	cout << "sundays: " << sundays << endl;
}
