#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

class Spy {
    public:
        string code;
        char location;
        int time;

        Spy(string code, char location, int time) {
            this->code = code;
            this->location = location;
            this->time = time;
        }
};

int main() {
    Spy s = Spy("aa",'a',0);
    cin >> s.code >> s.location >> s.time;
    cout << "secret code : " << s.code << endl
         << "meeting point : " << s.location << endl
         << "time : " << s.time;
    return 0;
}