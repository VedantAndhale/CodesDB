// Problem: Q. Coordinates of a Point
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Q
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
using namespace std;
int main()
{
	double x,y;
	cin>>x>>y;
	if (x!=0 && y==0 )
		cout<<"Eixo X";
	else if (x==0 && y!=0)
		cout<<"Eixo Y";
	else if (x>0 && y>0)
		cout<<"Q1";
	else if (x<0 && y>0)
		cout<<"Q2";
	else if (x<0 && y<0)
		cout<<"Q3";
	else if (x>0 && y<0)
		cout<<"Q4";
	else
		cout<<"Origem";
	return 0;
}