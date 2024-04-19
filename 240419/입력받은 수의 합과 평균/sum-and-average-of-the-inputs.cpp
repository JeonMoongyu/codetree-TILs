#include <iostream>
using namespace std;

int main() {
    int n, a, sum_val=0, cnt=0;
    cin >> n;
    for (int i=1; i<=n; i++){
        cin >> a;
        sum_val += a;
        cnt++;
    }
    cout << fixed;
    cout.precision(1);
    cout << sum_val << " " << (double)sum_val/cnt;
    return 0;
}