#include <iostream>
using namespace std;

int oddnumber(){
  
  int counter;
  int result = 0;
  
  for (counter = 1; counter<=20; counter = counter + 2)
  {
    cout <<counter <<" ";
  }

}
int main() {
  oddnumber();

  return 0;
}
