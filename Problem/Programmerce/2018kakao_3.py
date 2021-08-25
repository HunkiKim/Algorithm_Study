from collections import deque
def solution(cacheSize, cities):
    dq = deque()
    answer = 0
    if len(cities)==0:
        return answer
    elif len(cities)==1:
        return 5
    dq.append(cities[0].lower())
    answer += 5
    for i in range(1,len(cities)):
        city = cities[i].lower()
        if dq.count(city) and cacheSize>0:
            answer+=1
            idx = dq.index(city)
            del dq[idx]
            dq.append(city)
        else:
            if len(dq)<cacheSize:
                dq.append(city)
                answer += 5
            else:
                dq.popleft()
                dq.append(city)
                answer+=5
    return answer

solution(3, [
    "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo",
    "Seoul"
])
#30