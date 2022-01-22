#include <iostream>

int main()
{
    // Example 1
    std::cout << "Example 1" << std::endl;
    int a = 3;
    int b = 4;
    int c = a & b;
    int d = a | b;
    int e = a ^ b;
    std::cout << c << std::endl;
    std::cout << d << std::endl;
    std::cout << e << std::endl;
    std::cout << ~0 << std::endl;

    // Example 2
    std::cout << "Example 2" << std::endl;
    int x = 4;
    printf("%d\n", x << 3);
    printf("%d\n", x >> 1);

    return 0;
}
