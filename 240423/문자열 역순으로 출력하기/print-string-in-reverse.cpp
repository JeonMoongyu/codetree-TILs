#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr[4];
    for (int i=0; i<4; i++)
        cin >> arr[i];
    for (int j=3; j>=0; j--)
        cout << arr[j] << endl;
    return 0;
}