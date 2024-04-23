#include <iostream>
#include <string>
using namespace std;

void F() {
    for (int i=0; i<10; i++)
        cout << '*';
}

int main() {
    for (int i=0; i<5; i++){
        F();
        cout << endl;
    }
    return 0;
}