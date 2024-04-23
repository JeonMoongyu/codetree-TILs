#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b, s, t;
    cin >> a >> b;
    s = a + b;
    t = b + a;
    cout << stoi(s) + stoi(t);
    return 0;
}