import heapq
import sys

pq = []
cnt = 0
N = int(sys.stdin.readline())
for _ in range(N):
    a = int(sys.stdin.readline())
    if a == 0 and len(pq) == 0:
        print('0')
    elif a == 0:
        print(heapq.heappop(pq)[1])
    else:
        heapq.heappush(pq, (abs(a), a))
