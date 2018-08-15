#include <iostream>

using namespace std;

int n, m;
int map[8][8];
int maxsz;

bool isValid(int i, int j) {
  if (0 <= i && i < n )
    if (0 <= j && j < m)
      return true;
  return false;
}
typedef struct _pos {
  int i;
  int j;
}POS;

POS d[] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

void fill (int i, int j) { 
  
  for (int k = 0; k < 4; k++) {
    if (isValid(i + d[k].i, j +d[k].j) && map[i + d[k].i][j +d[k].j] == 0) {
      map[i + d[k].i][j + d[k].j] = 3;
      fill(i + d[k].i, j + d[k].j);
    }
  }
}

void printMap() {
  cout << "\n";
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cout << map[i][j] << " ";
    }
    cout << "\n";
  }
  cout << "\n";
}


int countSafe() {
  int c = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (map[i][j] == 0) {
        c++;
      }
    }
  } 
  return c;
}

void scan(int walls) {

  if (walls == 0) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (map[i][j] == 2) {
          fill(i, j);
        }
      }
    }
    
    int safe = countSafe();
    if (maxsz < safe) {
      maxsz = safe;
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (map[i][j] == 3) {
          map[i][j] = 0;
        }
      }
    }
    return ;
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (map[i][j]==0) {
        map[i][j] = 1;
        scan(walls-1);
        map[i][j] = 0;
      }
    }
  }
}

int main (void) {
  cin >> n >> m;
  // cout << n <<  m;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> map[i][j];
    }
  }

  scan(3);

  cout << maxsz;

}