#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b;
    cin >> a >>b;
    a += b;
    b += a;
    cout << a << " " << b;
    return 0;
}