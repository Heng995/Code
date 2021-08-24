#include <stdio.h>

#include <math.h>

int main (void)
{
    int a, b, c, x1, x2;
    scanf("%d %d %d", &a, &b, &c);

    if(b*b-4*a*c>0)
    {
        x1=(-b+(sqrt((b*b)-(4*a*c))))/(2*a);
        x2=(-b-(sqrt((b*b)-(4*a*c))))/(2*a);
        printf("Two different roots x1=%d , x2=%d\n", x1,x2);
    }

    if(b*b-4*a*c==0)
    {
        x1=(-b)/(2*a);
        printf("Two same roots x=%d\n", x1);
    }

    if(b*b-4*a*c<0)
    {
        printf("No real root\n");
    }

    return 0;
}