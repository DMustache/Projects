#include <iostream>

using namespace std;

int main()
{
    int n = 0, cur = 0, neg_counter = 0;
    int zero_p = -1, neg_max_i = -1, neg_max_val = -1000000001;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> cur;
        if (cur == 0)
            zero_p = i;
        if (cur < 0)
        {
            neg_counter++;
            if (neg_max_val < cur)
                neg_max_val = cur, neg_max_i = i;
        }

    }
    for (int i =0; i < n; i++)
        if (i != zero_p && neg_counter % 2 ==0 || i != neg_max_i)
            cout << i << ' ';
    return 0;
}