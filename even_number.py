#include <iostream>
using namespace std;

int evennumber(){
  
  int counter;
  int result = 0;
  
  for (counter = 2; counter<=20; counter = counter + 2)
  {
    cout <<counter <<" ";
  }
  
  return result;

}
int main() {
  evennumber();

  return 0;
}
