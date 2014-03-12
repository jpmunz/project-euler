#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream file;
	string line;

	file.open("problem22.txt");

	vector<string> lines;
	while(!file.eof())
	{
		getline(file, line, ',');
		lines.push_back(line.substr(1,line.length()-2));
	}

	file.close();

	sort(lines.begin(), lines.end());

	long long total = 0;
	for(int i = 0; i < lines.size(); i++)
	{
		int score = 0;
		for(int c = 0; c < lines[i].length(); c++)
			score += lines[i][c] - 'A' + 1;

		score *= (i+1);

		total += score;
	}

	cout << "Total: " << total << endl;
}
