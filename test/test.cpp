#include <cstdio>
#include <cstring>
char S[10000][500];
char tmp[500];

int n, m;
int main(void) {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++){
    scanf("%s", S[i]);
  }
  int count = 0;
  for (int j = 0; j < m; j++){
    scanf("%s", tmp);
    int len = strlen(tmp);
    for (int k = 0; k < n; k++) {
      if (strlen(S[k]) >= len) {
        if (strncmp(S[k], tmp, len)==0){
          count++;
          break;
        } 
      }
    }
  }
  printf("%d", count);
}