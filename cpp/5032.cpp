#include <iostream>
using namespace std;

int a,b,c;
int main(void) {
  cin >>a>>b>>c;

  int n = a+b;
  int count = 0;

  while (n >= c) {
    int m = n / c;
    n %= c;
    count += m;
    n += m;
  }
  cout << count;
}