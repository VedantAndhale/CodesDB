#include <iostream>
#include <string>
using namespace std;
int main()
{
   string first_name,last_name;
   cout << "Enter your First name : " << endl;
   getline(cin, first_name);
   cout << "Enter your Last name : " << last_name << endl;
   getline(cin, last_name);
   cout << "welcome " << first_name << " " << last_name << " to my world." << endl;
   return 0;
}