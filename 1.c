#include <stdio.h>

int main(void){
    int i = 0, 
        count = 0;

    for (i = 0; i < 1000; i++) {
        /* code */
        if (i % 3 == 0 ||i % 5 == 0){
            count += i;
        }
    }
    printf("%d", count);
}

     
