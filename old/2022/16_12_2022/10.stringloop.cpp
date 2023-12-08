#include <iostream>
#include <string>
using namespace std;
int main()
{
   char my_string[]="Hitesh";
   char my_name[] = {'H', 'i', 't', 'e', 's', 'h' , 0}; //both are same just rememeber 0
   printf("My name is %s\n",my_string);
   printf("My name is %s\n", my_name);

   cout<<"Take Break 1"<<endl;
   for (int i = 0; my_name[i]; i++)
   {
      cout<<"character is "<<my_name[i]<<endl;
   }

   cout<<"Take Break 2"<<endl;
   for (char *cp = my_name; *cp != 0; cp++)
   {
      cout<<"character is "<<*cp<<endl;
   }
   cout<<"Take Break 3"<<endl;
   for (char i:my_name)
   {
      if (i==0)
         break;
      cout << "character is " << i << endl;
   }
   return 0;
}