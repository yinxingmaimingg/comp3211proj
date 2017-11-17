#include <stdio.h>
#include <stdlib.h>

int main () {
   int i, n, j, temp;
   time_t t;
   
   n = 9;
   
   /* Intializes random number generator */
   srand((unsigned) time(&t));

   //for (j=0; j<n; j++){ 
      /* Print 10 random numbers from */
      for( i = 0 ; i < n ; i++ ) {
         temp = rand()%100 - 50;
         printf("%d ", temp);

      }
      printf("\n");
   //}   

   return(0);
}