#include <stdio.h>

int main(){

    while(1){
        int x,y,z;
        scanf("%d %d %d", &x, &y, &z);

        if(x == 0)
            break;

        int max = 0;
        if(max < x) max = x;
        if(max < y) max = y;
        if(max < z) max = z;

        if(max == x) x = 0;
        if(max == y) y = 0;
        if(max == z) z = 0;

        if(max*max == x*x + y*y + z*z)
            printf("right\n");

        else
            printf("wrong\n");
    }
    
}