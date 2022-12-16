#include <iostream>

using namespace std;
int main()
{
   int score = 200;
   int *myp = &score;

   printf("Value of card is : %d\n", score); //value
   printf("Value of card is : %p\n", myp);   //address

   int &another_score = score;
   another_score = 800;

   printf("Value of card is : %d\n", score);  //value
   printf("Value of card is : %p\n", myp); //address
   return 0;
}