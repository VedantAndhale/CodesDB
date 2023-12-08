#include <iostream>

using namespace std;
int main()
{
   int card = 40;
   int my_card = card;
   int *myp;
   myp = &card;
   my_card = *myp; //pointer dereferncing
   printf("Value of card is : %d\n", my_card); //value
   printf("Value of card is : %p\n", myp);   //address
   printf("Value of card is : %d\n", *myp);  //value
   printf("Value of card is : %p\n", &card); //address
   return 0;
}