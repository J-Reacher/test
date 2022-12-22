#include <stdio.h>

int fibonacci(int n)
{
    if (n <= 1)
        return n;
    printf("\t%d\n", n);
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int fibonacci_DP(int n) // Dynamic programming
{
    char f[1024];
    f[0] = 0;
    f[1] = 1;
    for (int i = 1; i < n; i++)
        f[i] = f[i - 1] + f[i - 2];
    return f[n];
}

int main()
{
    int result = fibonacci_DP(50);
    printf("%d\n", result);
    return 0;
}