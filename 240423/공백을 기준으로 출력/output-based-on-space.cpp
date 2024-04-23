#include <iostream>
#include <string>
using namespace std;

int main() {
    string str1, str2;
    getline(cin, str1);
    getline(cin, str2);
    int n=str1.length(), m=str2.length();
    for (int i=0; i<n; i++){
        if (str1[i]==' ')
            continue;
        cout << str1[i];
    }
    for (int i=0; i<m; i++){
        if (str2[i]==' ')
            continue;
        cout << str2[i];
    }

    return 0;
}