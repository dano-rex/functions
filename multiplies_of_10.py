#include <iostream>
using namespace std;

int multiply(){
  
  int counter;
  int result = 0;
  
  for (counter = 10; counter<=100; counter = counter + 10)
  {
    cout <<counter <<" ";
    
  }
  
  return result;

}
int main() {
  multiply();

  return 0;
}
