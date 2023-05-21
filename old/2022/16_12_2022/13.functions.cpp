#include <iostream>
using namespace std;

void sayHello(){
   puts("Hello Bro");
}
int saytwo(){
   return 2;
}
int main()
{
   sayHello();
   saytwo(); //wont print 2
   cout << (saytwo()+2)<<endl; //would print 2, check if type is int only typecast it to be wrong
   //cout << sayHello()<<endl; //would give error 
   return 0;
}


//https://stackoverflow.com/9248533/how-does-a-linker-know-what-all-libraries-to-link
//https://stackoverflow.com/questions/3322911/what-do-linkers-do
