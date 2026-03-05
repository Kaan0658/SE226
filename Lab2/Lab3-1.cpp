#include <iostream>
using namespace std;

int main() {
    int x;
    cout << "Enter a number which is greater then 1: ";
    cin >> x;
    if (x<=1) cout << "number is not greater then 1" << endl;
    else
        while (x>1) {
            if (x%2==0) {
                x=x/2;
                cout << x << endl;
            }
            else {
                x=x*3+1;
                cout << x << endl;
            }
        }
}
