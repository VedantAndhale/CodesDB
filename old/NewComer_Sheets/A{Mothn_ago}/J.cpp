// Problem: J. Multiples
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/J
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)
// tricky*****
#include<iostream>
using namespace std;
int main()
{
	int a,b;
	cin>>a>>b;
	if (a%b==0 || b%a==0)
		cout<<"Multiples";
	else
		cout<<"No Multiples";
	return 0;
}
