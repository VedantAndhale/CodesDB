// Problem: X. Two intervals
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/X
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
using namespace std;
int main()
{
	int A,B,a,b;
	cin>>A>>B>>a>>b;
	if(max(A,a)>min(B,b))
		cout<<-1;
	else
		cout<<max(A,a)<<" "<<min(B,b);
	return 0;
}