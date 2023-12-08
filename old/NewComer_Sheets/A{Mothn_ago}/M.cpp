// Problem: M. Capital or Small or Digit
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/M
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
using namespace std;
int main()
{
	char ch;
	cin>>ch;
	if(ch >= 65 && ch <= 90)
		cout<<"ALPHA\nIS CAPITAL";
	else if(ch >= 97 && ch <= 122)
		cout<<"ALPHA\nIS SMALL";
	else if(ch >= 48 && ch <= 57)
		cout<<"IS DIGIT";
	
	return 0;
}