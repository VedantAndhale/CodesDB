#include <iostream>
#include <string>

using namespace std;

class Man{
   string _name;
   int _age;
   Man(){}
   friend class Superman;
protected:
   Man(const string &name, const int &age): _name(name), _age(age){}
   void run() { puts("I can run"); }
public:
   void sayName() const;
};
void Man::sayName()const{
   cout << "My name is " << _name << " and age is " << _age << endl;
}

class Superman : public Man{
   bool flight;
public:
	Superman(string name) : Man(name, 26){}
	// void run() { puts("I can run light speed"); } //friend class use
	void run() { printf("I can run light speed%d\n",_age); }
};

class Spiderman : public Man{
   bool flight;
public:
	Spiderman(string name) : Man(name, 19){}
	void run() { puts("I can run normal speed"); }
};

int
main()
{
	Superman clark("Kent");
	clark.sayName();
	clark.run();

	Spiderman peter("Peter");
	peter.sayName();
	peter.run();
	return 0;
}