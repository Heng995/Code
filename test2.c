#include <stdio.h>
int main(void)
{
   int m;
   printf("Please into Month:");
   scanf("%d", &m);
   if(m<0 && m>5)
   printf("summer");

   return 0;
}