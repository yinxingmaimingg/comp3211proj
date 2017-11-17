#include<stdio.h>
void quicksort(int number[10],int first,int last){
   int i, j, pivot, temp;

   if(first<last){
      pivot=first;
      i=first;
      j=last;

      while(i<j){
         while(number[i]<=number[pivot]&&i<last)
            i++;
         while(number[j]>number[pivot])
            j--;
         if(i<j){
            temp=number[i];
            number[i]=number[j];
            number[j]=temp;
         }
      }

      temp=number[pivot];
      number[pivot]=number[j];
      number[j]=temp;
      quicksort(number,first,j-1);
      quicksort(number,j+1,last);

   }
}

int main(){
   int i, count, number[10];
   count = 10;
   //printf("How many elements are u going to enter?: ");
   //scanf("%d",&count);

   FILE *myFile;
   myFile = fopen("input.txt", "r");

   //read file into array
   

   for (i = 0; i < count; i++)
   {
       fscanf(myFile, "%d", &number[i]);
   }
/*
   printf("Enter %d elements: ", count);
   for(i=0;i<count;i++)
      scanf("%d",&number[i]);*/

   quicksort(number,0,count-1);

   //printf("Order of Sorted elements: ");
   for(i=0;i<count;i++)
      printf(" %d",number[i]);
   printf("\n");

   int min = number[0];
   for (i = 1; i<count; i++){
      if (number[i] < min){
         printf("false\n");
         break;
      }
      min = number[i];
   }

   printf("\n");

   return 0;
}