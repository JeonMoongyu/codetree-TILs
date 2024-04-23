#include <iostream>
using namespace std;

void F(int n) {
    for (int i=0; i<n; i++)
        cout << "12345^&*()_" << endl;
}

int main() {
    int n;
    cin >> n;
    F(n);
    return 0;
}