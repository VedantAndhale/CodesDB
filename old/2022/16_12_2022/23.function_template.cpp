#include <iostream>
#include <string>
// #include "23.header.h"
using namespace std;

// void lifeUp(int *life){
//    ++(*life);
// }
// int main()
// {
//    int life=3;
//    lifeUp(&life);
//    cout << life << endl;
//    return 0;
// }

//inside classes called methods
//call by method 1 = * & without them it is call by value
// call by refernce method 2
void lifeUp(int &life){
   ++life;
}
template<typename T>
T addme(T a,T b){
   return a + b;
}

int main()
{
   int life=3;
   lifeUp(life);
   cout << life << endl;

   int v1 = 4;
   int v2 = 5;
   float v3 = 5.6;
   float v4 = 7.5;
   cout << addme(v1, v2) << endl;
   cout << addme(v3, v4) << endl;
   return 0;
   
}
