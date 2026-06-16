#include <stdio.h>
double power(double x, unsigned int n, int *mult_count) {
    double res = 1.0;
    *mult_count = 0;
    while (n > 0) {
        if (n % 2 == 1) {
            res *= x;
            (*mult_count)++;
        }
        if (n > 1) {
            x *= x;
            (*mult_count)++;
        }
        n /= 2;
    }
    return res;
}
int main() {
    double x;
    unsigned int n;
    int mult_count;
    if (scanf("%lf %u", &x, &n) == 2) {
        double res = power(x, n, &mult_count);
        printf("%lf\n", res);
        printf("%d\n", mult_count);
    }
    return 0;
}
