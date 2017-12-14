#include <iostream>                     // Preprocessor Directive
using namespace std;                    // Using C＋＋ Standard Libeary
const int n = 9;                         //The number of terms of a polynomial
inline int fabs(int k)                     // Return the absolute value of k
{ 
    return k < 0 ? -k : k;
}
int main(void)                          // Main function
{ 
    int a[n];
    while (cin >> a[0]) {               // Input coefficients
        for (int i = 1; i < n; i++)  
            cin >> a[i];
        bool first = true;              // Set the mark for the first term
        for (int i = 0; i < n; i++)
            if (a[i]) {               //Output non-zero terms
                if (first) {           // Deal with the first term
                    if (a[i] == -1 && i < n - 1)    // The current term is -1
                        cout << '-';
                    else if (a[i] != 1 && i == n - 1)   // The current is not 1
                        cout << a[i];
                    if (i == n - 2) // MARK 1   If the exponent is 1, don’t output the exponent; else output the exponent.
                        cout << 'x';
                    else if (i < n - 1) // MARK 1
                        cout << "x^" << n - i - 1; // MARK 1
                    first = false;  // Reserve the mark of the first term of the polynomial
                } else {         //Output the sign and the absolute value
                    cout << ' ' << (a[i] < 0 ? '-' : '+') << ' ';  //Output the sign
                    if (fabs(a[i]) != 1 || i == n - 1)         //If the coefficient is 1, don’t output it
                        cout << fabs(a[i]);
                    if (i == n - 2) // MARK 2   If the exponent is 1, don’t output the exponent; else output the exponent.
                        cout << 'x';
                    else if (i < n - 1) // MARK 2
                        cout << "x^" << n - i - 1; // MARK 2
                }
            }
        if (first)                  // If all coefficients are 0, output 0.
            cout << 0;
        cout << endl;
    }
    return 0;
}
