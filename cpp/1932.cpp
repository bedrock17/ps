
#include <cstdio>

int arr [600][600];
int memo [600][600];
int n;

int f(int i,int j) {
	if (memo[i][j] == -1) {
		int a,b;
		if (i+1 == n-1) {
			a = arr[i+1][j];
			b = arr[i+1][j+1];
		} else {
			a = f(i+1, j);
			b = f(i+1, j+1);
		}
		if (a > b) {
			memo[i][j] = arr[i][j] + a;
		} else {
			memo[i][j] = arr[i][j] + b;
		}
	}

	return memo[i][j];
}

int main(void) {

	scanf("%d\n", &n);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
      scanf("%d", &arr[i][j]);
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			memo[i][j] = -1;
		}
	}

	printf("%d", f(0, 0));


}