#include <iostream>
using namespace std;

int main() {
    int age_1, age_2;
    char sex_1, sex_2;
    cin >> age_1 >> sex_1 >> age_2 >> sex_2;
    cout << ( age_1 >= 19 && sex_1 == 'M' || age_2 >= 19 && sex_2 == 'M' );
    return 0;
}