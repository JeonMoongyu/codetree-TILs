#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b, cnt=0;
    cin >> a >> b;
    string s = to_string(a+b);
    for (int i=0; s[i]!='\0'; i++){
        if (s[i]=='1')
            cnt++;
    }
    cout << cnt;
    return 0;
}