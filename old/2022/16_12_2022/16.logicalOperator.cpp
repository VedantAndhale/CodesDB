#include <iostream>
#include <string>
using namespace std;
int main()
{
   bool isFbUser = true;
   bool isGoogleUser = true;
   bool isAdmin = true;
   if ((isFbUser || isGoogleUser) && isAdmin)
   {
      puts("Welcome Admin");
   }
   else
   {
      puts("No admin access !");
   }if (isFbUser || isGoogleUser)
   {
      puts("Welcome User");
   }

   return 0;
}