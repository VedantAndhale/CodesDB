#include <iostream>
#include <string>
using namespace std;

template<typename T>
void func(T t){
   cout << "sigle func " << t << endl;
}
template<typename T ,typename... Args> ///args and arg can by ved lco ets
void func(T t, Args... args){
   cout << "Mulity value  func " << t << endl;
   func(args...);
}
int main()
{
   string myName = "hitesh";
   func(myName);
   func(1, 2, 3.4, 4.5, myName);
   return 0;
}

// ... = are variadic which we used in catch