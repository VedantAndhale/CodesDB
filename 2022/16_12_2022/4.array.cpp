#include <iostream>
#include <string>
using namespace std;
int main()
{
   int integer_array[4]={1,2,3,4}; 
   cout << integer_array[0] << endl; //value
   cout << integer_array << endl; //address

   int another_array[4];
   another_array[0] = 9;
   cout << another_array[0] << endl; //original value

   *another_array = 29;
   cout << another_array[0] << endl; //updated value

   cout << another_array[1] << endl; // value
   int *ap = another_array;
   ap++;
   *ap = 206;
   cout << another_array[1] << endl; // updated value
   return 0;
}