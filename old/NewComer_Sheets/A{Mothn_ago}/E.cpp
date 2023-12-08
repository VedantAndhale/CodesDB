// Problem: E. Area of a Circle
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/E
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    double r;
	double PI= 3.141592653;
	cin>>r;
	double area =PI*r*r;
	cout<< fixed <<setprecision(9)<<area;
	return 0;

}