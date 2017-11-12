#include <iostream>
using namespace std;
int foo(int param) 
{
  int k;
  for (k=0; k<10; k++) {
    cout<<k<<endl;
  }
  if (param)
  {
    return 1;
  }
  else 
  {
    return 0;
  }
}

int main(int argc, char* argv[]) {
  foo (0);

  return 0;
}