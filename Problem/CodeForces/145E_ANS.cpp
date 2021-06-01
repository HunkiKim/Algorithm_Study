#include <math.h>
#include <stdio.h>

#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <vector>
#define N 4100000
#define INF 1000000007
using namespace std;

int n4[N], n7[N], mx[N], my[N], sign[N];
int x, y;
char s[1200000];

void modify(int p) {  // 바꿋
  sign[p] = 1 - sign[p];
  swap(n4[p], n7[p]);
  swap(mx[p], my[p]);
}

void update(int p) {      //
  if (sign[p]) {          // sign[p]라면
    sign[p] = 0;          // 0으로 다시 바꾸고
    modify(p * 2);        // 수정
    modify((p * 2) + 1);  // 수정
  }
}

void refresh(int p) {
  int x = p * 2, y = x + 1;  // x-> 2 y -> 3 이런식으로 즉 build에서 했던 숫자들
  n4[p] = n4[x] + n4[y];  // n4[1] = n4[2] + n4[3] 이런식으로 n4가 몇개고
  n7[p] = n7[x] + n7[y];  // n7[1] = n7[2] + n7[3] n7이 몇개인지 업데이트
  mx[p] = max(mx[x] + n7[y],
              n4[x] + mx[y]);  // mx[1] = max(mx[2] + n7[3] , n4[x] + mx[3]) 444
                               // 7777 or 444 4777 이런식으로 비교
  my[p] = max(my[x] + n4[y],
              n7[x] + my[y]);  // my[1] = max(my[2] + n4[3], m7[2]+ my[3])
                               // 거꾸로 대기중 77744... 444444 or 77777774444
}

void buildTree(int p, int l, int r) {
  if (l == r) {            // l , r이 같다면
    n4[p] = s[l] == '4';   //  4 라면 1 아니라면 0
    n7[p] = s[l] == '7';   // 7 이라면 1 아니라면 0
    mx[p] = 1, my[p] = 1;  // 초기화 1로
    return;
  }

  int mid = (l + r) / 2;  // mid
  buildTree(p * 2, l, mid);
  buildTree((p * 2) + 1, mid + 1, r);  // 트리 만들기
  refresh(p);                          // 다 만들고 refresh
}

void change(int p, int l, int r) {
  if (l >= x && r <= y) {  // 범위 내에 있으면
    modify(p);             // 수정
    return;                // 종료
  }
  if (l > y || r < x) return;
  update(p);
  int mid = (l + r) / 2;
  change(p * 2, l, mid);
  change((p * 2) + 1, mid + 1, r);
  refresh(p);  //최댓 최솟값 초기화
}

int main() {
  //    ifstream in;
  //    in.open("/Users/Tom/Program/algo/programming_challenge/data/input.txt");
  //    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

  int n, m;

  scanf("%d%d", &n, &m);  // input n, m 넣기 m은 몇번 명령을 실행할 것인가
  scanf("%s", s + 1);  // s + 1 -> 즉 1부터 센다

  buildTree(1, 1, n);  // 트리 생성
  while (m--) {        // 0까지 돌렷
    scanf("%s", s);
    if (*s == 'c')  // count
      printf("%d\n", mx[1]);
    else {  // swich
      scanf("%d%d", &x, &y);
      change(1, 1, n);
    }
  }
}