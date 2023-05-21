// Problem: K. Max and Min
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/K
// Memory Limit: 64 MB
// Time Limit: 250 ms
// 
// Powered by CP Editor (https://cpeditor.org)
// min max func ****
#include<iostream>
using namespace std;
int main()
{
	int a,b,c;
	cin>>a>>b>>c;
	int minval = min(a, min(b, c)); 
	int maxval = max(a, max(b, c)); 
	cout<<minval<<" "<<maxval;
	return 0;
}

