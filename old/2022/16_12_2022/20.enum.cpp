#include <iostream>

using namespace std;
enum MsOffice : uint8_t //8_t to save memory
{
   BOLD = 1,
   ITALICS =7,
   UNDERLINE,
   CROSSED
};
int main()
{
   int myAttributes = UNDERLINE;
   cout << myAttributes << endl;
   return 0;
}

//its line auto ++