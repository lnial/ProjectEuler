#include <stdio.h>

int main(void){
    int array[3] = {1, 2, 0}, 
        count = 0, 
        i  = 0;

    while(1){
        array[2] = array[0] + array[1];


        printf("%d\n", array[2]);
        if (array[2] % 2 && array[2] < 4000000){
             count += array[2];
        }
        else if (array[2] > 4000000){
             // printf("%d\n", count);
             break;
        }
        array[0] = array[1];
        array[1] = array[2];

        /*if (i % 3 == 0 ||i % 5 == 0){*/
            /*count += i;*/
        /*}*/
    }
    printf("%d\n", count + 2);
}

     
