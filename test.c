#include <stdio.h>
#include <stdlib.h>
int main (void)
{
    int i=1, sum=0;
    while (sum<=100)
    {
        sum += i;
        printf("%2d=%2d\n", i, sum);
        i++;
    }
    printf("%d次", i-1);
    return 0;
}