#include <iostream>
using namespace std;

int F(int a, int b, int c) {
    if (a<=b && a<=c)
        return a;
    if (b<=c)
        return b;
    return c;
}

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << F(a,b,c);
    return 0;
}