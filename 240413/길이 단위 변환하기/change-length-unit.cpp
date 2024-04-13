#include <iostream>
#include <string>
using namespace std;

int main() {
    
    cout << fixed;
    cout.precision(1);

    double a = 9.2, b = 1.3;
    double p = 30.48, q = 160934;

    cout << a << "ft = " << a*p << "cm" << endl;
    cout << b << "mi = " << b*q << "cm"; 

    return 0;
}