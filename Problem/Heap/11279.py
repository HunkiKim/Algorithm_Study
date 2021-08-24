import sys
import heapq

pq = []
N = int(sys.stdin.readline())
for _ in range(N):
    a = int(sys.stdin.readline())
    b = -a
    if a == 0 and len(pq) == 0:
        print('0')
    elif a == 0:
        print(-heapq.heappop(pq))
    else:
        heapq.heappush(pq, b)
