#include <iostream>
using namespace std;
int main(){
   int n, k;
   cin >> n;
   k = 1;
   while (k*k < n)
      k = k + 1;
   cout << ((k-1) * (k - 1)) << ' ' << k;
   return 0;
}