#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

class Hero {
    public:
        string id;
        int level;

        Hero(string id="", int level=0){
            this->id = id;
            this->level = level;
        }

};

int main() {
    Hero h1=Hero(), h2=Hero();
    h1.id = "codetree";
    h1.level = 10;
    cin >> h2.id >> h2.level;
    cout << "user " << h1.id << " lv " << h1.level << endl
         << "user " << h2.id << " lv " << h2.level;
    return 0;
}