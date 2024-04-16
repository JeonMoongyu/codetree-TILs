#include <iostream>
using namespace std;

int main() {
    int m;
    if (m<=2)
        cout << "Winter";
    else if (m<=5)
        cout << "Spring";
    else if (m<=8)
        cout << "Summer";
    else if (m<=11)
        cout << "Fall";
    else
        cout << "Winter";
    return 0;
}