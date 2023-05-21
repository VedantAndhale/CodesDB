// Problem: R. Age in Days
// Contest: Codeforces - Sheet #1 (Data type - Conditions)
// URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/R
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<iostream>
using namespace std;
int main()
{
 int years, months, days;
   
 cin>>days;
   
 years = days / 365;
   
 months = days % 365 / 30;
   
 days = days % 365 % 30;
   
 cout<<years<<" years"<<endl;
 cout<<months<<" months"<<endl;
 cout<<days<<" days"<<endl;
   
 return 0; 
}