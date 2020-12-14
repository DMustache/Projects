#include <iostream>

using namespace std;

int main()
{
    int vecint = 0;
    int superDuperMin = 1001;
    int nMin = 1001;
    int superMin = 1001;
    int crnt = 0;
    int ans = 0;
    int minimum = 1001;
    cin >> vecint;
    for (int i = 0; i < vecint; i++)
    {
        cin >> crnt;
        if (crnt % 2 == 0)
        {
            if(crnt < superDuperMin && crnt < superMin && crnt < minimum)
            {
                minimum = superMin;
                superMin = superDuperMin;
                superDuperMin = crnt;
            }
            else if (crnt < superMin && crnt < minimum && crnt < superDuperMin)
            {
                minimum = superMin;
                superMin = crnt;
            }
            else if (crnt < superMin && crnt < minimum && crnt < superDuperMin)
            {
                minimum = crnt;
            }
        }
        else if(crnt % 2 != 0)
        {
            if (crnt < nMin && crnt < superMin)
            {
            nMin = superMin;
            superMin = crnt;
            }
        }
        else if (crnt < nMin && crnt < superMin)
        {
            nMin = crnt;
        }
    }
    ans = min((superDuperMin + superMin + minimum), (superDuperMin + superMin + nMin));
    if ((superDuperMin == 1001 || superMin == 1001 || minimum == 1001) && (superDuperMin == 1001 || nMin == 1001 || superMin == 1001))\
    {
        cout << 'None' << endl;
    }
}