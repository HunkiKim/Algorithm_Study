#include <stdio.h>

#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;
class Node {
 public:
  int l, r, nd, sum;
};

int A[200005];
Node T[200005];

int build(int nd, int n, int L, int R) {
  int mid;
  T[nd].r = R;
  T[nd].l = L;
  mid = (R + L) / 2;
  if (L == R) {
    T[nd].nd = A[L];
    return 0;
  }
  build(nd * 2, n, L, mid);
  build(nd * 2 + 1, n, mid + 1, R);
  T[nd].nd = T[nd * 2].nd + T[nd * 2 + 1].nd;
  return 0;
}

int update(int nd, int L, int R) {
    
}

int main() {
  int n, q, i, j;
  scanf("%d %d", &n, &q);
  A[0] = 0;
  for (i = 1; i <= n; i++) {
    scanf("%d", &A[i]);
  }
  for (i = 1; i <= n; i++) {
    scanf("%d %d", &T[i].l, &T[i].r);
    
  }
  build(1, n, 1, n);
  for (i = 1; i <= n; i++) {
    printf("%d\n", T[i].nd);
  }
}