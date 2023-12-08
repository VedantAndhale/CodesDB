#include <iostream>
#include <string>
using namespace std;
int main()
{
   string my_color;
   cout << "Enter Your Favourite Color : \n";
   getline(cin, my_color);
   cout << "Hey " << my_color << " is my favourite color too " << endl;
   
   return 0;
}
