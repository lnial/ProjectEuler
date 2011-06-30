#include <stdio.h>


int IsPrime(int n){
    int i;

    if(n < 2)
        return 0;
    else if(n == 2)
        return 1;

    if(n % 2 == 0)
        return 0;

    for(i = 3; i * i <= n; i += 2){
      if(n % i == 0){
        return 0;
      }
    }
    return 1;
}

int main(void)
{
  int i = 0, 
      j = 0;
  char array[10002] = {0};

  /*printf("%d", IsPrime(3));*/
  for (i = 2, j = 0; j < 10002; i++) {
    if (IsPrime(i) == 1){
      printf("%d\n", i);
      array[j] = i;
      j++;
    }
  }

  return 0;

}
