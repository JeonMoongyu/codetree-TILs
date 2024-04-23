#include <iostream>
#include <string>
using namespace std;

int main() {
    char a, b;
    cin >> a >> b;
    int n = (int)a, m = (int)b;
    cout << n+m << " ";
    cout << ((n>m)?n-m:m-n);
    return 0;
}