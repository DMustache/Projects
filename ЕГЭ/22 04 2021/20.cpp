#include <iostream>
using namespace std;
int main()
{
    int x, a, b, d;
    cin >> x;
    a = 0; b = 1;
    while (x > 0) {
        if (x % 2 > 0)
            a += x % 12;
        else
            b *= x % 12;
        x = x / 12;
        }
    cout << a << endl;
    cout << b << endl;
    return 0;
}