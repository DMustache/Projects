#include <vector>
#include <iostream>
#include <fstream>
#include <ctime>
#include <random>
using namespace std;
 
void gen()
{
    ofstream fs("data.txt");
    mt19937 mt(time(0));
    uniform_int_distribution<> dqtty(1, 400);
    uniform_int_distribution<> dnumber(1, 1000);
    int n = dqtty(mt);
    fs << n << endl;
    for (int i=0; i < n;i++)
        fs << dnumber(mt) << endl;
}
 
void ineff()
{
    int n=0;
    cin>>n;
    int mx(0);
    vector<int> nums(n,0);
    for (int i=0;i<n;i++) cin >>nums[i];
    for (int i=0;i<n;i++)
        for (int j=i+6;j<n;j+=6)
            if ((nums[i]+nums[j])%19 == 0)
                mx = max(mx, nums[i]+nums[j]);
    cout << mx << endl;
}
 
void eff()
{
 
}
 
int main()
{
    int mode(0);
    cin >> mode;
    switch(mode)
    {
        case 0: gen(); break;
        case 1: ineff(); break;
        case 2: eff(); break;
        default: cout << "ERROR" << endl;
    }
    /**if (mode == 0) gen();
    else if (mode == 1) ineff();
    else if (mode == 2) eff();
    else cout << "ERROR" << endl;
*/
}