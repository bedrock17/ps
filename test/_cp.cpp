#include <stdio.h>

long long int n;

int sqrt(long long int);

int main()
{
  scanf("%lld", &n);
  printf("%d\n", sqrt(n));
}
#define LL long long
int sqrt(LL n){
  LL right = 2LL<<31-1;
  LL left = 1;
  
  if (right*right <= n) return right;

  while (left<right) {
    LL mid = (right+left)/2;
    LL tmp = mid*mid;
    LL tmp2 = (mid-1)*(mid-1);
    // printf("left %lld mid %lld right %lld        tmp2 : %lld, n : %lld, tmp : %lld \n", left, mid, right, tmp2, n, tmp);

    if (tmp == n) return mid;
    else if (tmp2 <= n && n < tmp) return mid-1;
    else if (tmp > n) {
      right=mid;
    } else {
      left=mid;
    }
  }
  return -1;
}