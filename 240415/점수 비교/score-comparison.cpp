#include <iostream>
using namespace std;

int main() {
    int a_m, a_e, b_m, b_e;
    cin >> a_m >> a_e >> b_m >> b_e;
    cout << (a_m>b_m && a_e>b_e);
    return 0;
}