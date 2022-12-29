// Problem: P. First digit !
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/P
// Memory Limit: 64 MB
// Time Limit: 250 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
#include <math.h>
using namespace std;
int main()
{
	int a,b,c,d;
	cin>>a;
	b=sizeof(a);
	c=pow(10,(b-1));
	d=a/c;
	if (d%2==0)
		cout<<"EVEN";
	else
		cout<<"ODD";
	return 0;
}