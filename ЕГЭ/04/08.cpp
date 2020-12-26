#include <iostream>

using namespace std;

int main() {
    int s = 15,  n = 99;
    while( n > s )
    {
        s = s + 3;
        n = n - 2;
    }
    cout <<n;
    return 0;
}