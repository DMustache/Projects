//https://inf-ege.sdamgia.ru/problem?id=7321
#include <iostream>

using namespace std;

int main ()
{
    int iteration;
    int time, timerUp, timerDown, iterationTime;
    int minRoad, varUp, varDown, i;
    cin >> iteration;
    cin >> time;
    iterationTime = 0;
    minRoad = time;
    for (int i = 0; i < iteration; i++)
    {
        cin >> timerUp >> timerDown;
        iterationTime = iterationTime + timerUp;
        varUp = minRoad + timerDown;
        varDown = iterationTime + time;
        if (varUp < varDown)
            minRoad = varUp;
        else
            minRoad = varDown;
    }
    cout << minRoad << endl;
    return 0;
}