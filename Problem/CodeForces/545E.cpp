#include <stdio.h>

#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;
class tpl {
 public:
  int b, w, EN;
  // edge번호를 찍어야하기 때문에
};
vector<tpl> ED[300005];

long long SL[300005];  // shortest path 저장 메모리
int ENU[300005];       // edgenumber
int ELE[300005];       // Edge length를 기록

class pkt {
 public:
  long long l;      // total path length
  int w, a, b, EN;  // w->weight a->s b->e en->num
  bool operator<(const pkt& k) const { return l > k.l; }
};

priority_queue<pkt> Q;
int Visit[300005];
int Dij(int s) {
  pkt p, q;
  int i;
  p.l = 0;
  p.w = 0;
  p.a = 0;
  p.b = s;
  p.EN = 0;
  Q.push(p);
  while (!Q.empty()) {
    p = Q.top();
    Q.pop();

    if (Visit[p.b]) {
      if (p.l == SL[p.b] && p.w < ELE[p.b]) {
        ELE[p.b] = p.w;
        ENU[p.b] = p.EN;
      }
      continue;  // visit했으면 무시
    }
    Visit[p.b] = 1;
    SL[p.b] = p.l;
    ENU[p.b] = p.EN;
    ELE[p.b] = p.w;
    for (i = 0; i < ED[p.b].size(); i++) {
      q.l = SL[p.b] + ED[p.b][i].w;
      q.w = ED[p.b][i].w;
      q.a = p.b;
      q.b = ED[p.b][i].b;
      q.EN = ED[p.b][i].EN;
      Q.push(q);
    }
  }
}
int n, m, u;

int main() {
  int i, j, A, B, W;
  tpl tmp;
  long long ans;
  scanf("%d %d", &n, &m);
  for (i = 1; i <= m; i++) {
    scanf("%d %d %d", &A, &B, &W);
    tmp.b = B;
    tmp.w = W;
    tmp.EN = i;
    ED[A].push_back(tmp);
    tmp.b = A;
    tmp.w = W;
    tmp.EN = i;
    ED[B].push_back(tmp);
  }
  scanf("%d", &u);
  Dij(u);  // u에서 시작하는 다익스트라
  ans = 0;
  for (i = 1; i <= n; i++) {
    if (i != u) ans += ELE[i];
  }
  printf("%lld\n", ans);
  for (i = 1; i <= n; i++) {
    if (i != u) printf("%d ", ENU[i]);
  }
  return 0;
}