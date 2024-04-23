#include <iostream>
using namespace std;

int F(int n) {
    int sum_val=0;
    for (int i=1; i<=n; i++)
        sum_val += i;
    return sum_val/10;
}

int main() {
    int n;
    cin >> n;
    cout << F(n);
    return 0;
}