#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n = 0;
    cin >> n;
    int minsum = 1000;
    int tmp = 0;

    vector<int> nums(n,0);
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        nums.push_back(tmp);
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            for (int jj = j; jj < n; jj++)
            {
                if (nums[i] != nums[j] && nums[i] != nums[jj] && nums[j] != nums[jj])
                    cout << nums[i] << nums[j] << nums[jj];
            }
        }
    }
}