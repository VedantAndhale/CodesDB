#include <iostream>
#include <string>
using namespace std;
string api_call(){
   return "Got some data from web\n";
};
int another_api_call(){
   return 5;
};
int main()
{
   auto response = api_call();
   auto rep = another_api_call();
   cout << "API response is " << response<<endl;
   cout << "API response is " << rep<<endl;
   if (typeid(response) == typeid(string))
   {
      puts("Type of Both ID matches\n");
   }
   if (typeid(rep) == typeid(string))
   {
      puts("Type of Both ID matches\n");
   }else{
      puts("Type of Both ID didn't matches\n");
   }
   if (typeid(rep) == typeid(int))
   {
      puts("Type of Both ID matches int\n");
   }
   return 0;
}
