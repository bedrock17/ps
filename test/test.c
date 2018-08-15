#include <stdio.h>

long long memo[10010]={1,};

int main(void)
{
  int a, b;
  int maxNum;
  long long maxCnt = 0;
  long long cnt = 1;
  scanf("%d %d", &a, &b);

  for(int i = a; i <= b; ++i)
  {
    cnt = 1;
    long long n = i;
    while(n != 1)
    {
      if(memo[n] != 0)
      {
        cnt += memo[n];
        break;
      }
      else
      {
        if(n % 2 == 1)
        {
          n = 3 * n + 1;
        }
        else if(n % 2 == 0)
        {
          n = n / 2;
        }
        cnt++;
      }
    }

    memo[i] = cnt;
    if(maxCnt < cnt)
    {
      maxCnt = cnt;
      maxNum = i;
    }
  }

  printf("%d %lld", maxNum, maxCnt);
  return 0;
}