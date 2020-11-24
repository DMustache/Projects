#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <random>
#include <ctime>

using namespace std;

void gen()
{
    ofstream fs("data.txt");
    mt19937 mt(time(0));
    uniform_int_distribution<> dqtty(1, 400);
    uniform_int_distribution<> dnumber(1, 1000);
    int n = dqtty(mt);
    cout << n << endl;
    for(int i = 0; i < n; i++)
        fs << dnumber(mt) << endl;
}

int main()
{
    ofstream f1("data.txt");
    f1 << 5;
    f1.close();
    ifstream f2("data.txt");
    int k = 0;
    f2 >> k;
    cout << k << endl;
    f2.close();
}