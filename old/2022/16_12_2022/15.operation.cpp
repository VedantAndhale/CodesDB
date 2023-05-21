#include <iostream>
 using namespace std;
int main()
{
   int life = 3;
   int points = 4;
   int score = 2;
   score += points;
   cout << score << endl;
   if(life != 5){
      puts("Into the if block");
   }
   return 0;
}