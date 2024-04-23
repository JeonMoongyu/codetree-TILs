#include <iostream>
using namespace std;

int main() {
    int n, sum_val=0;
    cin >> n;
    for (int i=1; i<=n; i++){
        sum_val += i;
        if (sum_val>=n){
            cout << i;
            break;
        }
    }
    return 0;
}