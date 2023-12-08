#include <iostream>

using namespace std;

void swap(int &a , int &b){
      int temp = move(a);
      a = move(b);
      b = move(temp);
}//  no new memory for temp will act as refernce
string printMe(){
      return "I am print";
}

int main()
{
      int a = 3;
      int b = 5;
      swap(a, b);
      cout << "A: " << a << endl;
      cout << "B: " << b << endl;
      string s = printMe();//l and r value
      string &&ss = printMe();
      return 0;
}