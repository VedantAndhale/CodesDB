// Problem: H. Two numbers
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/H
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)
//have a look unique*****
#include<iostream>
#include <cmath> // lib needed to use
using namespace std;
int main()
{
	double a,b;
	cin>>a>>b;
	cout<<"floor "<<a<<" / "<<b<<" = "<<floor(a/b)<<endl;
	cout<<"ceil "<<a<<" / "<<b<<" = "<<ceil(a/b)<<endl;
	cout<<"round "<<a<<" / "<<b<<" = "<<round(a/b)<<endl;
	return 0;	
}