#include <iostream>
#include <string>
using namespace std;

class User{ //for deccelaring only variables you can use struct.

private: //by default
   int _secret = 22;
public:
   string name = "default";
   /*
   void classMessage(){
      cout << "class is great, " << name << endl;
   }*/

   void classMessage();
   void setSecert(const int &newsecret)
   {
      _secret = newsecret;
   }

   //int getSecret() { return _secret; }//generally as data type as we want to return some thing
   //int getSecret()const { return _secret; } int getSecret()const { return _secret; } //for const user rock dont deo eveywhere
   int getSecret()const; //lets get outside of class
};
int User::getSecret()const { 
   return _secret;
}
void User::classMessage(){
      cout << "class is great, " << name << endl;
}

int main()
{
   User sam;
   sam.name = "sam";
   sam.classMessage();
   sam.setSecert(333);
   cout << sam.getSecret() << endl;

   User hitesh;
   hitesh.classMessage();
   hitesh.name = "hitesh";
   hitesh.classMessage();

   const User rock;
   cout << rock.getSecret()<<endl;

   User peter = sam;
   cout << peter.getSecret() << endl;

   return 0;
}


//https://stackoverflow.com/questions/4172722/what-is-the-rule-of-three

