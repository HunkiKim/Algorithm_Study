#include <stdio.h>

#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;
#define LL long long

class Node {
 public:
  LL fgasu;  // 4 개수
  LL sgasu;  // 7 개수
  LL LR;     // left to right
  LL RL;     // right to left
};

int main() {
  LL n, m, i;
  string s, cond;
  string cnt = "count";
  string swi = "switch";
  scanf("%lld %lld", &n, &m);
  cin >> s;
  for (i = 1; i <= n; i++) {
    cin >> cond;
    if (cond[1] == 's') {
      countf();
    } else {
      switchf();
    }
  }
}