#include <stdio.h>
#include <stdlib.h>
int main (void)
{
    int i, conut = 0;

    for(i=1;i<=10000;i++)
        if((rand()%6+1) == 3)
        conut++;
    printf("擲10000次骰子時，出現3點的次數為%d次\n", conut);
    printf("機率為%.3f\n", (float)conut/10000);

    system("pause");
    return 0;
}