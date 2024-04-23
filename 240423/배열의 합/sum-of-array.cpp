#include <iostream>
using namespace std;

int main() {
    int arr[4][4];
    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            cin >> arr[i][j];
        }
    }
    int sum_val[4]={};
    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            sum_val[i] += arr[i][j];
        }
    }
    for (int i=0; i<4; i++)
        cout << sum_val[i] << endl;
    return 0;
}