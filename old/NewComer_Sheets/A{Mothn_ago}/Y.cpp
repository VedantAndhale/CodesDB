// Problem: Y. The last 2 digits
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Y
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
using namespace std;
int main()
{
	long long a,b,c,d,x;
	cin>>a>>b>>c>>d;
	a=a%100;
	b=b%100;
	c=c%100;
	d=d%100;
	x=(a*b*c*d)%100;
	if(x<10)
		cout<<0<<x;
	else
		cout<<x;
	return 0;
}
