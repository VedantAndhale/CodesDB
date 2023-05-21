// Problem: O. Calculator
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/O
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// new prob
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
using namespace std;
int main()
{
	long long A,B;
	char S;
	cin>>A>>S>>B;
	if(S=='+') 
		cout<<A+B;
	else if(S=='-') 
		cout<<A-B;
	else if(S=='*') 
		cout<<A*B;
	else if(S=='/') 
		cout<<A/B;
	
	
	return 0;
}