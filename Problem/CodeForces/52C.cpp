#include <stdio.h>

#include <algorithm>
#include <cstdio>

using namespace std;

#define LL long long
LL A[200005];  // 입력을 받을 배열

int n, m;
class Node {
 public:
  LL l, r, minim, incre;  // 각노드의 l, r은 내 아래쪽에
                          //몇번노드까지 잇는지
                          // minim 내 아래쪽의 최솟값
  //사실 이 모든값이 incre 만큼 변해야한다
  // 내 아래값들이
};

Node T[1000000];

LL build(LL nd, LL left, LL right) {  // nd는 노드번호
                                      //노드 번호에서 시작을 해서
  // left번호 부터 right 번호까지를 넣고 만들어라
  LL mid;          //
  T[nd].l = left;  // 현재 노드의 좌하단 노드는 left
  T[nd].r =
      right;  // 우 하단 노드는 right 1, 1, n에서 시작 T[1].l = 1 T[1].r = n
  T[nd].incre = 0;  // 증가는 다 0으로 설정
  if (left == right) {
    T[nd].minim = A[left];
    printf("%lld left %lld nd\n", left, nd);
    return 0;
  }
  mid = (left + right) / 2;
  build(nd * 2, left, mid);           // 왼쪽은 빌드를 두번
  build(nd * 2 + 1, mid + 1, right);  //
  T[nd].minim = min(T[nd * 2].minim + T[nd * 2].incre,
                    T[nd * 2 + 1].minim + T[nd * 2 + 1].incre);
  return 0;
}
LL query(LL nd, LL left, LL right) { // rmq 그 서아에서 최솟값을 찾아서 리턴
  LL lrt, rrt; // 
  if (left <= T[nd].l && right >= T[nd].r) { // 
    return T[nd].minim + T[nd].incre;
  }
  if (left > T[nd].r || right < T[nd].l) { // 범위가 맛이 간 경우
    return (LL)5000000000000;
  }
  lrt = query(nd * 2, left, right); // 왼쪽 트리
  rrt = query(nd * 2 + 1, left, right); // 오른쪽 트리
  return min(lrt, rrt) + T[nd].incre; // 둘중에 더 작은값 리턴 + 변화율
}

LL update(LL nd, LL left, LL right, LL val) { // inc
  LL lrt, rrt; // 
  if (left <= T[nd].l && right >= T[nd].r) { // 범위 내일 경우 
    T[nd].incre += val; // 노드들
    return 0;
  }
  if (left > T[nd].r || right < T[nd].l) return 0;
  update(nd * 2, left, right, val);
  update(nd * 2 + 1, left, right, val);
  T[nd].minim = min(T[nd * 2].minim + T[nd * 2].incre,
                    T[nd * 2 + 1].minim + T[nd * 2 + 1].incre);
  return 0;
}

int main() {
  // 1. build
  // 2. increment
  // 3. query
  // why
  LL i, lf, rg, v, m, lrt, rrt, rt;
  char c;
  scanf("%lld", &n);  // lld는 써도
  for (i = 1; i <= n; i++) {
    scanf("%lld", &A[i]);
  }
  build(1, 1, n);  // index tree 만들기
  for (i = 1; i <= n; i++) printf(" %d ", T[i].minim);

  printf("\n");
  scanf("%lld", &m);               // 몇번 조건 쓸 것인가
  for (i = 1; i <= m; i++) {       // 조건 몇번 쓸지
    scanf("%lld %lld", &lf, &rg);  //
    lf++;  // 배열이 1부터 시작하니까 조건 설정
    rg++;  // 같음
    c = getchar();
    if (c == '\n') {   // rmq
      if (lf <= rg) {  // lf <= rg 라면 그대로 진행하면됨 lf~rg
        rt = query(1, lf, rg);  // 1=루트 lf rg 찾아서 진행
        printf("%lld\n", rt);   // 진행 끝나면 rt로 뱉기
      } else {                  // 만약 lf>rg 라면 재설정 필요
        lrt = query(1, 1, rg);  //
        rrt = query(1, lf, n);  //
        printf("%lld\n", min(lrt, rrt));
      }
    } else {  // inc
      scanf("%lld", &v);
      if (lf <= rg) {
        update(1, lf, rg, v);
      } else {
        update(1, 1, rg, v);
        update(1, lf, n, v);
      }
    }
  }
  return 0;
}