#include <iostream>
using namespace std;
int F(int x) {
    return abs(x-3) + abs(x+3) + 7;
}
int main() {
    int a, b, M, R;
    a = -20; b = 20;
    M = a; R = F(a);
    for(int t = a; t <= b; t++)
        if (F(t) < R) {
        M = t;
        R = F(t);
        }
    cout << M+R;
    return 0;
}