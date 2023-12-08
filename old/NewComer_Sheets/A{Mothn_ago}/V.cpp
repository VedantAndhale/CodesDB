// Problem: V. Comparison
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/V
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
using namespace std;
int main()
{
	int a,b;
	char s;
	cin>>a>>s>>b;
	switch (s)
	{
		case '=':
			if(a==b) cout<<"Right";
			else cout<<"Wrong";
			break;
		case '<':
			if(a<b) cout<<"Right";
			else cout<<"Wrong";
			break;
		case '>':
			if(a>b) cout<<"Right";
			else cout<<"Wrong";
			break;
	}
	return 0;
}