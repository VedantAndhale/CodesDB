#include <iostream>

using namespace std;
struct User{
   const int uId;
   const char *name;
   const char *email;
   int course_count;
};
int main()
{
   User mickey = {001,"mickey","mickey@cartoon.com",2};
   User donald = {002,"donald","donald@cartoon.com",3};
   User *d = &donald;
   // mickey.uId(001) old way
   cout << mickey.email << endl;
   cout << donald.name << endl<< donald.email<<endl;
   d->course_count = 12;
   cout << donald.course_count << endl;
   // can change namaae and email as only pointer is conts. in case of uID value is conts
   return 0;
}