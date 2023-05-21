// Problem: W. Mathematical Expression
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/W
// Memory Limit: 256 MB
// Time Limit: 250 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
using namespace std;
int main()
{
	int a,b,c,x;
	char s,q;
	cin>>a>>s>>b>>q>>c;
	if(s=='+')
		x=a+b; 
	else if (s=='-')
		x=a-b;
	else if (s=='*')
		x=a*b;
	if(c==x)
		cout<<"Yes";
	else
		cout<<x;
				
	return 0;
}