#include <iostream>
#include <string>
using namespace std;

class Phone{
   string _name = "";
   string _os = "";
   int _price = 0;
public:
   Phone(); // default constructor if made pvt no access
   Phone(const Phone &);//copy constructor
   Phone(const string &name, const string &os, const int &price); //parameter constructor
   string getName() { return _os; }
   ~Phone();//destructor
};

Phone::Phone() : _name(), _os(), _price(){
   puts("default constructor");
}

Phone::Phone(const string &name, const string &os, const int &price) : _name(name), _os(os), _price(price){
   puts("Parameterized constructor");
}

Phone::Phone(const Phone &values){
   puts("Overwrite Copy constructor");
   _name = "new - " + values._name;
   _os = "Skinned - " + values._os;
   _price = values._price;
}
Phone ::~Phone(){
   printf("Destructor called for %s\n", _name.c_str());
}

int main()
{
   Phone samsungA1;
   cout << samsungA1.getName() << endl;

   Phone OnePlus("Op8", "android-oxy", 7999);
   cout << OnePlus.getName() << endl;

   Phone OnePlus8 = OnePlus;
   cout << OnePlus8.getName() << endl;
   return 0;
}