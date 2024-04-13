#include <iostream>
#include <string>
using namespace std;

int main() {
    
    cout << fixed;
    cout.precision(6);

    int w = 13;
    double g = 0.165;

    cout << w << " * " << g << " = " << w*g;

    return 0;
}