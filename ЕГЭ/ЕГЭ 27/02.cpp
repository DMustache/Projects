#include <iostream>
#include <string>
#include <vector>

using namespace std;

int input()
{
    int n = 0, tmp = 0;
    cin >> n;
    vector<vector<int>> maxpairs(6, vector<int>(2, -1));
    vector<vector<int>> maxslices(6, vector<int>(2, -1));
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        int maxslices = 0;
        int curslices = i % 6;
        if (tmp > maxpairs[curslices][0] || tmp > maxpairs[curslices][1])
            maxslices[i][0] = maxslices[i][1];
            maxslices[i][0] = tmp;
    }
    int maxpars = 0;
    for (int i = 1; i < 6; i++)
    {
        int maxpair = 0;
        int curpair = maxslices[i][0] + maxslices[i][1];
        if (maxpairs < curpair)
            maxpairs = curpair;
    }
    cout << maxpairs << endl;
    return 0;
}