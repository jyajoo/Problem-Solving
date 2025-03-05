'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/17680

< [1차] 캐시 >
'''
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    for i in cities:
        city = i.lower()
        if city not in q:
            if len(q) == cacheSize:
                if cacheSize != 0:
                    q.popleft()
                else:
                    answer += 5
                    continue
            q.append(city)
            answer += 5
        else:
            q.remove(city)
            q.append(city)
            answer += 1
    
    return answer