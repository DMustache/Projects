#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main () {
  vector<int> myints = {1,2,3};

  sort (myints.begin(),myints.end());

  cout << "The 3! possible permutations with 3 elements:\n";
  do {
    cout << myints[0] << ' ' << myints[1] << ' ' << myints[2] << endl;
  } while ( next_permutation(myints.begin(),myints.end()) );

  cout << "After loop: " << myints[0] << ' ' << myints[1] << ' ' << myints[2] << '\n';

  return 0;
}