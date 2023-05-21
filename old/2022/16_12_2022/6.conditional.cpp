#include <iostream>
#include <string>
using namespace std;
int main()
{
   int rating = 5;
   if(rating==5)
   {
      puts("5 star rated");
   }
   else if(rating==4)
   {
      puts("not 4");
   }
   else
   {
      puts("Not 5 star rated");
   }
   printf("Your rating feedback is %s\n", rating < 4 ? "true block" : "false block");

   return 0;
}


/*
condition : if else
            if elseif elseif
            ternary operator : condition ? "true block" : "false block"
*/