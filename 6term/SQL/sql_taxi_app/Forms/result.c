#include <stdio.h>
#include <math.h>

float a,x;
int vlfct;

int factorial(int count){
    vlfct=1;
    for (int i=1;i<=count;i++)
        vlfct=vlfct*i;
    return vlfct;
}

int main(int agrc,char *argv[]){
    int x = 8;
    printf("'x' = %d", x);
    printf("\n");
    int result = factorial(x);
    printf("factorial(%d) = %d", x,result);
    return 0;
}