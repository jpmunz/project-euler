#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main()
{
	ifstream file;
	string line;

	file.open("problem13.txt");

	vector<string> lines;
	while(!file.eof())
	{
		getline(file, line);
		lines.push_back(line);
	}

	file.close();

	int digits = lines[0].length() - 1;
	int	digits_in_sum = 10;

	long long sum = 0;
	bool hit_mark = false;

	for(int d = digits; d >= 0; d--)
	{
		double add = 0;
		for(int l = 0; l < lines.size(); l++)
			add += atoi(lines[l].substr(d,1).c_str());

		if(hit_mark)
			add *= pow(10, digits_in_sum - 1);
		else
			add *= pow(10, digits - d);

		sum += (long long)add;

		if((int)(sum / pow(10,digits_in_sum)) > 0)
		{
			sum /= 10;
			hit_mark = true;
		}

	}

	cout << "sum: " << sum << endl;
}
