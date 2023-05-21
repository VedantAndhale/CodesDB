#include <iostream>

// #define NULL 0
using namespace std;
void printVal(int a)
{
   printf("Integer Value is %d\n",a);
}
void printVal(double a){
   printf("Integer Value is %f\n",a);
}
void printVal(int *a){
   printf("Pointer Value is %p\n",a);
}
int main()
{
   printVal(5);
   printVal(5.3);
   // printVal(NULL);
   printVal(nullptr);

   return 0;
}