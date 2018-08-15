

#include <cstdio>
#include <cstring>
int dp[2][100001] = {0};
int arr[2][100001] = {0};
int n;
int m;
int f(int i, int j) {
  if (j >= m - 1) {
    return arr[i][m-1];
  }
  if (dp[i][j] < 0) {
    int nxti = i ? 0 : 1;
    int a = f(nxti, j+1);
    int b = f(nxti, j+2);
    dp[i][j] = (a > b ? a : b) + arr[i][j];
  }
  return dp[i][j];
}
int main(void) {
  scanf("%d", &n);
  for (int i = 0;i<n;i++) {
    scanf("%d", &m);
    for (int j=0;j<m;j++){
      scanf("%d", &arr[0][j]);
      dp[0][j]=-1;
      dp[1][j]=-1;
    }
    for (int j=0;j<m;j++){
      scanf("%d", &arr[1][j]);
      
    }
    int a = f(0, 0);
    int b = f(1, 0);
    printf("%d\n", a>b?a:b);
  }
  return 0;
}