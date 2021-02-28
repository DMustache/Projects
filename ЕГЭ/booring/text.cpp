#include <iostream>
using namespace std;
int main()
{
    int x, a, b, ans;
    for (int x = 999999; x > 0;x--){
        a = 0; b = 1;
        while (x > 0)
        {
            a++;
            if (x%12 != 0){
                b *= x%12;}
            x = x / 12;
            cout << x << endl;
        }
    }
    if (a == 2 && b == 12)
        ans++;
    cout << ans;
    return 0;
}