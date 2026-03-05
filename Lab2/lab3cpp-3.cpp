#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a number which is between 3 and 9 inclusive: " << endl;
    cin >> n;
    if (n<3 or n>9)
        cout << "number is not between those two numbers";
    else {
        for (int i=1; i<n; i++) {
            for (int j=1; j<=i; j++) {
                cout <<"*";
            }
            cout << endl;
        }
        for (int i=n; i>0; i--) {
            for (int j=1; j<=i; j++) {
                cout <<"*";
            }
            cout << endl;
        }
    }
}