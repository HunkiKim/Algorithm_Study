#include <stdio.h>

#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;
int n, q;
char S[100005];
class Node {
 public:
  int l, r, cnt, lazy;
};
Node T[26][400005];
int pullup(int t, int nd) {
  T[t][nd].cnt = T[t][nd * 2].cnt + T[t][nd * 2 + 1].cnt;
  return 0;
}

int build(int t, int nd, int L, int R) {
  int mid;
  T[t][nd].l = L;
  T[t][nd].r = R;
  T[t][nd].lazy = -1;
  if (L == R) {
    if (S[L] - 'a' == t)
      T[t][nd].cnt = 1;
    else
      T[t][nd].cnt = 0;
    return 0;
  }
  mid = (L + R) / 2;
  build(t, nd * 2, L, mid);
  build(t, nd * 2 + 1, mid + 1, R);
  pullup(t, nd);
  return 0;
}
int pushdown(int t, int nd) {
  int lazy = T[t][nd].lazy;
  if (lazy == 1) {
    T[t][nd * 2].lazy = 1;
    T[t][nd * 2].cnt = T[t][nd * 2].r - T[t][nd * 2].l + 1;
    T[t][nd * 2 + 1].lazy = 1;
    T[t][nd * 2 + 1].cnt = T[t][nd * 2 + 1].r - T[t][nd * 2 + 1].l + 1;
  } else if (lazy == 0) {
    T[t][nd * 2].lazy = 0;
    T[t][nd * 2].cnt = 0;
    T[t][nd * 2 + 1].lazy = 0;
    T[t][nd * 2 + 1].cnt = 0;
  }
  T[t][nd].lazy = -1;
}
int query(int t, int nd, int L, int R) {
  int lrt, rrt;
  if (T[t][nd].l >= L && T[t][nd].r <= R) return T[t][nd].cnt;
  if (T[t][nd].l > R || T[t][nd].r < L) return 0;
  pushdown(t, nd);
  lrt = query(t, nd * 2, L, R);
  rrt = query(t, nd * 2 + 1, L, R);
  return lrt + rrt;
}

int update(int t, int nd, int L, int R, int V) {
  if (T[t][nd].l >= L && T[t][nd].r <= R) {
    if (V == 1) {
      T[t][nd].cnt = T[t][nd].r - T[t][nd].l + 1;
      T[t][nd].lazy = 1;
    } else {
      T[t][nd].cnt = 0;
      T[t][nd].lazy = 0;
    }
    return 0;
  }
  if (T[t][nd].l > R || T[t][nd].r < L) return 0;
  pushdown(t, nd);
  update(t, nd * 2, L, R, V);
  update(t, nd * 2 + 1, L, R, V);
  pullup(t, nd);
  return 0;
}

int main() {
  int i, j, l, r, v, left;
  int num[26];
  scanf("%d %d", &n, &q);
  scanf(" %s", S + 1);
  for (i = 0; i < 26; i++) build(i, 1, 1, n);
  for (i = 0; i < q; i++) {
    scanf("%d %d %d", &l, &r, &v);
    for (j = 0; j < 26; j++) {
      num[j] = query(j, 1, l, r);
      update(j, 1, l, r, 0);
    }
    if (v == 1) {
      left = l;
      for (j = 0; j < 26; j++) {
        if (num[j] > 0) {
          update(j, 1, left, left + num[j] - 1, 1);
        }
        left += num[j];
      }
    } else {
      left = l;
      for (j = 0; j < 26; j++) {
        if (num[25 - j] > 0) update(25 - j, 1, left, left + num[25 - j] - 1, 1);
        left += num[25 - j];
      }
    }
  }
  // print
  for (i = 1; i <= n; i++) {
    for (j = 0; j < 26; j++) {
      if (query(j, 1, i, i) == 1) putchar('a' + j);
    }
  }
  putchar('\n');
  return 0;
}