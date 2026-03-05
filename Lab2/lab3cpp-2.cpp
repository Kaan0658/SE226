#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a number which is between 10 and 100 inclusive: ";
    cin >> n;
    if (n<10 or n>100)
        cout << "number is not between those two numbers";
    else{
        int FbCount=0;
        int FCount=0;
        int BCount=0;
        while (n>0) {
            if (n%7==0) {
                n=n-1;
                continue;
            }
            if (n%15==0) {
                cout << "FizzBuzz" << endl;
                FbCount=FbCount+1;
                n=n-1;
            }
            else if (n%3==0) {
                FCount=FCount+1;
                cout << "Fizz" << endl;
                n=n-1;
            }
            else if (n%5==0) {
                BCount=BCount+1;
                cout << "Buzz" << endl;
                n=n-1;
            }
            else {
                cout << n << endl;
                n=n-1;
            }
        }
            cout<< "---Summary---" << endl;
            cout << "Fizz count is:" << FCount << endl;
            cout << "Buzz count is:" << BCount << endl;
            cout << "FizzBuzz count is:" << FbCount << endl;
        }
    }