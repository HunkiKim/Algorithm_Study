#include <stdio.h>

#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> ED[1000005];

int main() {
  int i, j, n, u, v;
  cin >> n;
  for (i = 1; i < n; i++) {
    cin >> u >> v;
    ED[u].push_back(v);
    ED[v].push_back(u);
  }
  int ans = 1000005;

  for (i = 1; i < n; i++) {
    j = ED[i].size();
    ans = min(ans, j);
  }
  printf("%d", ans);
}
