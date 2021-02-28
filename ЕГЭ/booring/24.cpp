#include
using namespace std;
int main()
{
int s = 4
int n;
int n1 = 0, n2 = 0, n3 = 0, n4 = 0;
int a_;
int cnt;
cin >> n;
cnt = 0;
for (int i = 0; i < n; ++i)
{
	cin >> a_;
	if (i >= s)
	{
		if (a_ % 29 == 0)
		cnt += i - s + 1;
		else
		cnt += n4;
	}
	n4 = n3;
	n3 = n2;
	n2 = n1;
	if (a_ % 29 == 0)
		n1 += 1;
}
cout << cnt;
return 0;
}