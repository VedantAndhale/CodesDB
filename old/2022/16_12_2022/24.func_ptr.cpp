#include <iostream>
#include <string>
using namespace std;
int getTwo(){
   return 2;
}
void intersting(){
   puts("I am interesting");
}
int main()
{
   int whatIgot = getTwo();
   void (*pointsToInteresting)() = intersting;
   cout << whatIgot << endl;
   pointsToInteresting();
   (*pointsToInteresting)();
   return 0;
}