#include <iostream>
#include <cstdint> //for fixed size
using namespace std;
int main()
{
   //1 byte is of 8 bit
   printf("Size of %ld\n",sizeof(long)*8);
   int fun = 0x16; //hexdecimal
   cout << fun << endl;
   fun = 0b00010110; //binary
   cout << fun << endl;
   return 0;
}