#include <stdio.h>

#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;
int A[100005];
int T[100005];
int B[100005];
int C[100005];
int V[100005];

void Tree(int r, int n, int s, int e) {}
int main() {
  int n, a, b, c, i, j;
  cin >> n;
  for (i = 1; i <= n; i++) {
    cin >> A[i];
  }
  for (i = 1; i <= n; i++) {
    cin >> B[i];
  }
  T[1] = B[n - 1];  // root
}