#include <iostream>
using namespace std;
int main() {
    int s = 150,  n = 0;
    while( s + n < 300 )
    {
        s = s - 5;
        n = n +25;
    }
    cout <<n;
    return 0;
}