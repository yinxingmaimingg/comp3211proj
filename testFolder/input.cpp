#include <iostream>
#include <cstdlib>
#include <ctime>
#include <sys/time.h>
using namespace std;

int main () {
   int i, n, j, temp;
   time_t t;
   
   n = 9;
   
   /* Intializes random number generator */

   timeval tv;
   gettimeofday(&tv, 0);
   //cout<<(long int)(tv.tv_usec)<<endl;
   srand((long int)(tv.tv_usec));

   //for (j=0; j<n; j++){ 
      /* Print 10 random numbers from */
      for( i = 0 ; i < n ; i++ ) {
         temp = rand()%20 - 10;
         if (rand()%10<5) {
            temp = 0;
         }
         cout<<temp<<" ";

      }
      cout<<endl;
   //}   

   return(0);
}