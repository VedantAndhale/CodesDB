#include<iostream>
#include<string>
#include<cstdlib>
#include<ctime>
using namespace std;
void play()
{
    int random = rand()%251;
    cout<<"Lets satart"<<endl;
    cout<<random <<endl;
    cout<<"Guess a number : ";
    while(true)
    {
        int guess;
        cin>>guess;
        if(guess==random)
        {
            cout<<"You Won!\n";
            break;
        }
        else if(guess<random)
        {
            cout<<"Better Luck Next time, It's too low\n";
        }
        else 
        {
            cout<<"Better Luck Next time, It's too High\n";
        }
    }
}
int main()
{
    int choice;
    do
    {
        srand(time(NULL));
        cout<<"\n0.quit \n1. play game\n";
        cin>>choice;
        switch(choice)
        {
            case 0:
                    cout<<"Thanks for trying out";
                    return 0;
            case 1:
                play();
                break;
        }
    }while(choice!=0);
    return 0;
}