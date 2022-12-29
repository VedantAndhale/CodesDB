// Problem: Z. Hard Compare
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Z
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// pow() use can give error some time : out of bonds or other memory error
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	long long a,b,c,d;
	cin>>a>>b>>c>>d;
	cout<<(b*log(a)>d*log(c)?"YES":"NO");
	return 0;
}
