#include <iostream>
using namespace std;
int main()
{
    int s = 9; //между элементами
    int n;
    int h1 = 0, h2 = 0, h3 = 0, h4 = 0;
    int tmp; // новое значение
    int cnt; //кол-во пар
    cin >> n;
    cnt = 0;
    for (int i = 0; i < n; ++i)
    {
        cin >> tmp;
        if (i >= s)
        {
            if (tmp % 29 == 0)
            {
                cnt += i - s + 1;
            }
            else
            {
                cnt += h4;
            }
        }
        h4 = h3;
        h3 = h2;
        h2 = h1;

        if (tmp % 29 == 0)
        {
            h1 += 1;
        }
    }
    cout << cnt;
    return 0;
}