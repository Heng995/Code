#include <stdio.h>
#include <stdlib.h>
int main (void)
{
    printf("1.\n");
    for(int i=0;i<10;i++)//次數//
    {
        int j = 0;
        while(j<=i)//while*//
        {
            printf("* ");
            j++;
        }
        printf("\n");
    }
    printf("\n");

    printf("2.\n");
    for(int i=0;i<10;i++)//次數//
    {
        for(int j=10;j>i;j--)//for//
        {
            printf("* ");
        }
        printf("\n");
    }
    printf("\n");

    printf("3.\n");
    for(int i=0;i<10;i++)//次數//
    {
        for(int k=9;k>i;k--)//for空//
        {
            printf("  ");
        }
        for(int j=0;j<=i;j++)
        {
            printf("* ");
        }
        printf("\n");
    }
    printf("\n");

    printf("4.\n");
    for(int i=0;i<10;i++)
    {
        int k=1;
        while (k<=i)
        {
            printf("  ");
            k++;
        }
        for(int j=10;j>i;j--)
        {
            printf("* ");
        }
        printf("\n");
    }
    printf("\n");

    printf("5.\n");
    for(int i=0;i<=10;i++)
    {
        for(int j=10;j>i;j--)
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

    printf("6.\n");
    for(int i=0;i<10;i=i+2)
    {
        for(int j=0;j<=i;j++)
        {
            printf("*  ");
        }
        printf("\n");
 
    }
    for(int i=0;i<12;i=i+2)
    {
        for(int j=11;j>i;j--)
        {
            printf("*  ");
        }
        printf("\n");
    }
    printf("\n");
    system("pause");
    return 0;
}     