#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cin >> str;
    int n = str.length();
    str.erase(n-2,1);
    str.erase(1,1);
    cout << str;
    return 0;
}