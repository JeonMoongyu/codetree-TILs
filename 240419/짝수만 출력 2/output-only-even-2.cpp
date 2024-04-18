#include <iostream>
using namespace std;

int main() {
    int b, a;
    cin >> b >> a;
    int i = b;
    while ( i >= a ){
        cout << i << " ";
        i -= 2;
    }
    return 0;
}