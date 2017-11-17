#include <iostream>
using namespace std;
int max(int num1, int num2) {
   // local variable declaration
   int result;
 
   if (num1 > num2)
      result = num1;
   else
      result = num2;
 
   return result; 
}

int main(int argc, char* argv[]) {
  cout<< max(4, 8) <<endl;

  return 0;
}