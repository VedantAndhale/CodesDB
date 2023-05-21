#include <iostream>

using namespace std;
int main()
{
    int r,l,b,n;
    cin>>n;
    switch (n) 
    {
        case 1:
            cout<<"R = ";
            cin>>r;
            cout<<3.14*r*r;
        break;
        case 2:
            cout<<"L = ";
            cin>>l;
            cout<<"B = ";
        cin>>b;
        break;
    }
    return 0;
}