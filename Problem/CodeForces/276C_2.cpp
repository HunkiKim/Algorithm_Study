#include <stdio.h>

#include <algorithm>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
class Node {
 public:
  int l, r;
};

Node T[200005];

int S[200005];
long long B[200005];
int update(int L, int R, vector<int> C) {}

int main() {
  // clock_t start, finish;
  // start = clock();
  int n, q, i, j, ma, temp, ma2;
  long long ans = 0;
  cin >> n >> q;

  vector<int> C(n + 1, 0);
  vector<long long> A(n + 1, 0);

  for (i = 1; i <= n; i++) {
    cin >> A[i - 1];
  }

  for (i = 0; i < q; i++) {
    cin >> T[i].l >> T[i].r;
    C[T[i].l - 1]++;
    C[T[i].r]--;
  }
  for (i = 1; i < n; i++) C[i] += C[i - 1];

  sort(C.rbegin(), C.rend());
  sort(A.rbegin(), A.rend());
  // finish = clock();
  // cout << finish - start << "msec" << endl;

  for (i = 0; i < n; i++) {
    ans += C[i] * A[i];
  }
  cout << ans << endl;
  // finish = clock();
  // cout << finish - start << "msec" << endl;
}