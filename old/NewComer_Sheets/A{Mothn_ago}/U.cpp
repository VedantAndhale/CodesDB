// Problem: U. Float or int
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/U
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	float x;
	cin>>x;
	int y =(int)x;
	if (x-y>0)
		cout<<"float"<<" "<<y<<" "<< fixed <<setprecision(3)<<x-y;
	else
		cout<<"int"<<" "<<x;
	return 0;
}