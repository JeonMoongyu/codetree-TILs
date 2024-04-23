#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cin >> str;
    int n = str.length();
    cout << str[0] + str.substr(2,n-4) + str[n-1]; 
    return 0;
}