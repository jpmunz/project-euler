#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <limits>
#include <vector>
#include <queue>

using namespace std;

class Node
{
public:
	int dist_to;
	Node* best_neighbour;
	map<Node*, int> neighbours;

Node();
};

Node::Node()
: dist_to(-numeric_limits<int>::infinity()) 
{}

int main()
{
	ifstream file;
	string line;

	file.open("problem67.txt");

	vector<Node*> nodes;

	Node initial = Node();
	initial.dist_to = 0;

	int line_num = 1;
	int num_nodes = 0;
	for(;;)
	{
		if(file.eof()) break;
		getline(file, line);

		for(int n = 0; n < line_num; n++)
		{
			Node* new_node = new Node();
			nodes.push_back(new_node);
		}

		vector<int>distances;

		char* tokens = (char*)line.c_str();
		char* num;

		num = strtok(tokens, " ");
		while(num != NULL)
		{
			distances.push_back(atoi(num));
			num = strtok(NULL, " ");
		}

		if(num_nodes == 0)
		{
			initial.neighbours[nodes[0]] = distances[0];
		}
		else
		{
			int d = 0;
			for(int r = num_nodes - line_num + 1; r < num_nodes; r++)
			{
				nodes[r]->neighbours[nodes[num_nodes+d]] = distances[d];
				nodes[r]->neighbours[nodes[num_nodes+d+1]] = distances[d+1];

				d++;
			}
		}

		num_nodes += line_num;
		line_num++;
	}

	file.close();


	vector<Node*> unfinished;
	unfinished.push_back(&initial);

	int best_path = 0;
	while(!unfinished.empty())
	{
		int next_highest_value = -1;
		int next_highest_index = 0;
		Node* cur_node;

		for(int i = 0; i < unfinished.size(); i++)
		{
			if(unfinished[i]->dist_to > next_highest_value)
			{
				next_highest_value = unfinished[i]->dist_to;
				next_highest_index = i;
				cur_node = unfinished[i];
			}
		}

		unfinished.erase(unfinished.begin()+next_highest_index);

		map<Node*, int>::iterator n;

		for(n = cur_node->neighbours.begin(); n != cur_node->neighbours.end(); n++)
		{
			Node* next = n->first;
			int dist = n->second;
			
			int attempt = dist + cur_node->dist_to;

			if(attempt > next->dist_to)
			{
				next->dist_to = attempt;
				next->best_neighbour = cur_node;

				if(attempt > best_path)
					best_path = attempt;
			}

			unfinished.push_back(next);
		}
	}

	cout << "best path: " << best_path << endl;
}



