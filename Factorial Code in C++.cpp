#include <iostream>
using namespace std;

// Function to calculate factorial
int factorial(int n) {
    if (n == 0) 
        return 1; // Base case
    else 
        return n * factorial(n - 1); // Recursive case
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num; // Input from user
    cout << "Factorial: " << factorial(num) << endl; // Output result
    return 0;
}
