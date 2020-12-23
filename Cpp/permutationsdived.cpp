#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n = 0, tmp = 0;
    cin >> n;

    vector<vector<int>> maxpairs(6, vector<int>(2, -1));
    for(int i = 0; i < n; i++)
    {
        cin >> tmp;
        int cureslice = i % 6;
        if (tmp > maxpairs[cureslice][0])
        {
            maxpairs[cureslice][1] = maxpairs[cureslice][0];
            maxpairs[cureslice][0] = tmp;
        }

        else if(tmp == maxpairs[cureslice][0])
            maxpairs[cureslice][1] = maxpairs[cureslice][0];
    }
    int res = -1;
    for(int i = 0; i < 6; i++)
    {
        int curpair = 0;
        curpair = maxpairs[i % 6][0] + maxpairs[i % 6][1];
        if (curpair > res)
            res = curpair;
    }
    cout << res << endl;
    return 0;
}