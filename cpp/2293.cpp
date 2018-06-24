
// a, b = map(int, input().split())

// arr = []

// for i in range(a):
//   arr.append(int(input()))


// count = 0

// def f(n, m):
//   global count
  
//   if n < 0:
//     return

//   if n == 0:
//     count += 1
//     return
  
//   for i in range(m, a):
//     f(n - arr[i], i)
  
// # print(arr)
// f(b, 0)

// print(count)

#include <iostream>
using namespace std;

int arr[10000];
int memo[10000];
int a, b;

int f(int n, int m) {
  int c = 0;
    
  for (int i = m; i < a; i++) {
    if (n - arr[i] < 0) {
    
    } else if (n - arr[i] == 0) {
      
    } else if (memo[n-arr[i]] != -1) {
      // c += memo[n-arr[i]];
      c += 1;
    } else {
      memo[n - arr[i]] = f(n - arr[i], i);
      c += memo[n - arr[i]];
    }
  }
  
  return c;
}

int main(void) {
  cin >> a >> b;

  for (int i = 0; i < a; i++) {
    cin >> arr[i];
  }
  for (int i = 0; i < 10000; i++) {
    memo[i] = -1;
  }

  cout << f(b, 0);

  cout << endl;
  for (int i = 0; i < b; i++) {
    cout << i << " " << memo[i] << endl;
  }

}