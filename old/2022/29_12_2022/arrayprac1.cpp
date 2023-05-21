#include<iostream>
using namespace std;
int main()
{
    int n,a[200];
    cin>>n;
    for(int i=0;i<n;++i)
        cin>>a[i];
/*  code 1
    int max=0;
    for(int i=1;i<n;++i)
        if(a[max]<a[i])
            max=i;
    int max1=a[max];
    a[max]=-1000000;
    max=0;
    for(int i=1;i<n;++i)
        if(a[max]<a[i])
            max=i;
    int max2=a[max];
*/

    int max1,max2;
    if(a[0]>=a[1])
        max1=a[0],max2=a[1];
    else
        max1=a[1],max2=a[0];
    for(int i=2;i<n;++i)
        if(max1<=a[i])
            max2=max1,max1=a[1];
        else
            max2=a[i];

    cout<<"ans\n"<<max1<<endl<<max2<<endl;
    return 0;
}