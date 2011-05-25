#include <stdio.h>

int main(void){
    int maxFactor = 0, 
        primeFactor = 13195, 
        count = 0, 
        i  = 0,
        iw = 0, 
        arrayPrimeFactor[100];
    
    printf("%d\n", count);
    while(1){
        break;
        count++;
        
        printf("%d\n", count);
        if (primeFactor % count == 0){
            /*all primeFactor*/ 
            for (iw = count; iw > 0; iw--) {
                if (count % arrayPrimeFactor[iw] == 0){
                    printf("not primeFactor\n");
                    break;
                }
                else{
                    /*array into primeFactor*/
                    arrayPrimeFactor[i] = count;
                    i++;
                }
            }
            
            /*if (maxFactor < count){*/
                 /*maxFactor = count;*/
                 /*printf("%d\n", count);*/
            /*}*/
        }

        if (count == primeFactor){
             break;
        }
    }
    printf("%d\n", maxFactor);
}

     
