// Problem: N. Char
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/N
// Memory Limit: 64 MB
// Time Limit: 250 ms
// extra
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
#include <cctype>
using namespace std;
int main()
{
	char ch;
	cin>>ch;
	if(isupper(ch))
		cout<<(char)tolower(ch);
	else if(islower(ch))
		cout<<(char)toupper(ch);
	return 0;
}