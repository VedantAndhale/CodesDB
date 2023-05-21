#include <iostream>
#include <string>
using namespace std;
int factorial(int n);
int main()
{
   //factorial:5*4*3*2*1
   //factorial:1*2*3*4*5
   int n;
   cout << "Enter a value : ";
   cin >> n;
   cout << "your result for factorial is " << factorial(n) << endl;
   return 0;
}
int factorial(int n){
   if(n>1)
   {
      return n *factorial(n - 1);
   }
   else
   {
      return 1;
   }

}