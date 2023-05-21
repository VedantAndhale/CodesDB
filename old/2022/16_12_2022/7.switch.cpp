#include <iostream>
#include <string>
using namespace std;
int main()
{
   int rating = 3;
   switch (rating)
   {
   case 1:
      puts("1*");
      break;
   case 2:
      puts("2*");
      break;
   case 3:
      puts("3*");
      break; //if you dont use break there will be a fall through its automically controlled in may lang 
   case 4:
      puts("4*");
      break;
   case 5:
      puts("5*");
      break;
   default:
      puts("rate from 1 to 5");
      break;
   }
   return 0;
}