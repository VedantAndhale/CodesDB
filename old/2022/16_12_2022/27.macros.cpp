#include <iostream>
#define end return 0;
#define endmessage cout<<"Bye Macros" //used endmessage or end in Uppercases mostly
#define LCOINT int32_t
#define console_log(a) cout<<a<<endl
using namespace std;

int main()
{
   LCOINT a = 4; //use of macros to make program efficient
   console_log(a);
   cout << "Hello macro\n";
   endmessage;
   end // ; with 0 is bad practice of consistency
}