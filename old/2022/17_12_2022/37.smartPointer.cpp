#include <iostream>
#include <string>
#include <memory>
using namespace std;

class User{
public:
   User(){
        cout << "User created\n";
        }
   ~User(){
        cout << "User Destroyed\n";
        }
   void testfunc(){
        cout << "I am Test function\n";
   }
};
int main()
{
   {
      //   unique_ptr<User> sam(new User()); //non fav way of devs
        unique_ptr<User> sam = make_unique<User>();
        sam->testfunc();
      //   unique_ptr<User> samm = sam; //not allowed
   }
   {
      // shared_ptr<User> tim (new User()); //bad practice
      shared_ptr<User> tim = make_shared<User>();
      weak_ptr<User> wtim = tim; //to keep track
      shared_ptr<User> timm = tim;
   }
   cout<< "outside code\n";
   return 0;
}

//New-allocates
// Delet-Deallocates
//automatic memory management =smart pointer





