#include <stdio.h>

//加法//
int add(int n1, int n2) 
{
    int a;
    a=n1+n2;
    return a;
}

//絕對值//
int abs (int n)
{
    if(n<0)
        return -n;
    else
        return n;
}

//次方//
double power(double x, int n)
{
    int i;
    double p = 1.0;
    for(i=1;i<=n;i++)
        p=p*x;
    return p;
}

//質數//
int is_prime(int num)
{
    int i;
    for(i=2;i<=num-1;i++)
        if(num%i==0)
            return 0;
    return 1;
}

