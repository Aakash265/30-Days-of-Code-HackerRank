#include<iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;

    if (n%2 != 0)
    {
        cout<<"Weird";
    }
    else if (n%2 == 0 && n>=2 && n<=5)
    {
        cout<<"Not Weird";
    }
    else if (n%2 == 0 && n>=6 and n<=20)
    {
        cout<<"Weird";
    }
    else
    {
        cout<<"Not Weird";
    }
}