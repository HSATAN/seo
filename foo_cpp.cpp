#include<iostream>
using namespace std;
class TestLib
{
    public:
    void display();
    void display(int a);

};
void TestLib::display()
{
    cout<<"fist display"<<endl;
}
void TestLib::display(int a){
    cout<<"second display"<<a<<endl;

}
extern "C"{
TestLib obj;
void display(){
obj.display();}
void display_int(){
obj.display(98);
}

}