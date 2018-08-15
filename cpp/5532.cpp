#include <iostream>
#include <algorithm>
using namespace std;

int l,a,b,c,d;
int main(void) {

  cin>>l;cin>>a;cin>>b;cin>>c;cin>>d;
  cout << min(l-(a % c == 0 ? a/c : a/c+1), l-(b % d == 0 ? b/d : b/d +1));
}
