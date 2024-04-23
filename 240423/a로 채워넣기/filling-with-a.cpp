#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cin >> str;
    str[1] = 'a';
    int n = str.length();
    str[n-2] = 'a';
    cout << str;
    return 0;
}