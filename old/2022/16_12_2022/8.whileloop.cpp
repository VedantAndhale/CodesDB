#include <iostream>
#include <string>
using namespace std;
int main()
{
   int array[]={1,2,3};
   int i = 0;
   while (i < 3)
   {
      cout << "number" << array[i] << endl;
      i++;
   }
   cout<<"**********Next loop***********"<<endl;
   do
   {
      cout << "number " << array[i] << endl;
      i++;
   } while (i < 3); // mostly use for driver programs
   return 0;
}


/*
while loop , do while
brak , continue .

*/