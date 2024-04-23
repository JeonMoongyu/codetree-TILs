#include <iostream>
using namespace std;

void F(int *x) {
    for (int i=0; i<50; i++){
        if (x[i]%2==0)
            x[i] /= 2;
    }
}

int main() {
    int n;
    cin >> n;
    int arr[50];
    for (int i=0; i<n; i++)
        cin >> arr[i];
    F(arr);
    for (int i=0; i<n; i++)
        cout << arr[i] << " ";
    return 0;
}