#include <stdio.h>
#include <stdlib.h>
int main (void)
{
    for(int i=0;i<5;i++)//次數//
    {
        int j = 0;
        while(j<=i)//while*//
        {
            printf("*");
            j++;
        }
        printf("\n");
    }
    for(int i=0;i<=5;i++)
    {
        for(int j=5;j>i;j--)
        {
            printf(" ");
        }
        for(int k=0;k<=i;k++)
        {
            printf("* ");
        }
        printf("\n");
    }
    printf("\n");
}