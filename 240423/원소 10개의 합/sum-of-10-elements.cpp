#include <iostream>
using namespace std;

int main() {
    int arr[10];
    int sum_val=0;
    for (int i=0; i<10; i++){
        cin >> arr[i];
        sum_val += arr[i];
    }
    cout << sum_val;
    return 0;
}