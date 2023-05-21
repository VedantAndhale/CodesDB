// Problem: D.  Difference
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/D
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
using namespace std;
int main ()
{
	long long a,b,c,d;
	cin>>a>>b>>c>>d;
	long long x = (a*b)-(c*d);
	cout<<"Difference = "<<x;
}