#include <iostream>
#include <string>
using namespace std;

string palindrome(string &s) {
    string t="";
    int n = s.length();
    for (int i=n-1; i>=0; i--)
        t = t+s[i];
    return t;
}

int main() {
    string s;
    cin >> s;
    cout << ( s==palindrome(s) ? "Yes" : "No" );
    return 0;
}