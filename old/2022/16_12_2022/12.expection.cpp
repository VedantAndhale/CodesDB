#include <iostream>
using namespace std;
int main()
{
   // int call_api = 2;
   // float call_api = 2;
   char call_api = 'h';
   try
   {
      cout << "trying to use API value\n";
      cout << "Did some testing with api value\n";
      throw call_api;
      cout << "No code execute after return and throw";
   }
   catch (int x){
      cout << "integer exception handled\n";
   }
   catch (float x){
      cout << "float exception handled\n";
   }
   catch(...){
      cout << "something went wrong\n";
   }
   cout << "Keep on moving with rest of code\n";
   return 0;
}