#include <iostream>

int main()
{
    // Example 1
    std::cout << "Example #1" << std::endl;
    float a, b;
    a = 0.1;
    b = 0.2;
    float c = a + b;
    std::cout <<  "C: " << c << std::endl;
    // What is the expected output?
    std::cout << (c == 0.3) << std::endl;
    
    // Example 2
    std::cout << "Example #2" << std::endl;
    int x = 2147483647;
    // What is the expected output?
    std::cout << x + 1  << std::endl;

    // Example 3
    std::cout << "Example #3" << std::endl;
    float p = 3.14;
    float q = 0.000001;
    // What is the expected output?
    std::cout << (p - q) << std::endl;
}
