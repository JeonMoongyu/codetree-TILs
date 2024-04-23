#include <iostream>
using namespace std;

bool is_desired(int n) {
    return n%2==0 && (n/10+n%10)%5==0;
}

int main() {
    int n;
    cin >> n;
    cout << ( is_desired(n) ? "Yes" : "No" );
    return 0;
}