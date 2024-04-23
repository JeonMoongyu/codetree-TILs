#include <iostream>
#include <string>
using namespace std;

class Bomb {
    public:
        string code;
        char color;
        int second;

        Bomb(string code="", char color='\0', int second=0){
            this->code = code;
            this->color = color;
            this->second = second;
        }
};

int main() {
    Bomb b=Bomb();
    cin >> b.code >> b.color >> b.second;
    cout << "code : " << b.code << endl
         << "color : " << b.color << endl
         << "second : " << b.second;
    return 0;
}