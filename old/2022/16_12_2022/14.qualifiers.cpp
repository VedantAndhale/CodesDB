//https://stackoverflow.com/9248533/how-does-a-linker-know-what-all-libraries-to-link
//https://stackoverflow.com/questions/3322911/what-do-linkers-do
//linker info above

#include <iostream>
using namespace std;
int lifeUp(){
   static int life = 3;
   return ++life;
}
int main()
{
   int life = 3;
   cout << "Your Starting game life is " << life << endl;
   life = lifeUp();
   printf("Your updated game life is %d\n", life);
   life = lifeUp();
   printf("Your updated game life is %d\n", life);
   return 0;
}

/*
qualifiers
modification q: const,volatile,mutable
life duration q: static, register ,extern, auto(depriciated)

*/