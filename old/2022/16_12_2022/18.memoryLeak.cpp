#include <iostream>
#include <string>
using namespace std;
int main()
{
   int *myp;
   try
   {
      myp =new int[100];
      cout << "Memory Space allocated\n";
      //delete myp for simple int
   }catch(...){
      cout << "no allocationof memory\n";
   }//best practice
   delete[] myp; // for arrays
   int x = 3;
   x << 5; //lrft shit read more about left shit and right shift if needed
   return 0;
}

//read more on memory leak from refernce material