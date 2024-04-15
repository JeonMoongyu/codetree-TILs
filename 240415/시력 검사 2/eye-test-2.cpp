#include <iostream>
using namespace std;

int main() {
    double v;
    cin >> v;
    if (v>=1.0)
        cout << "High";
    else if (v>=0.5)
        cout << "Middle";
    else
        cout << "Low";
    return 0;
}