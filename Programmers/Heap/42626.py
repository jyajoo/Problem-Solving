'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42626

< 더 맵게 >
'''

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        
        if min1 >= K:
            return cnt
        
        cnt += 1
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + min2 * 2)
    
    min1 = heapq.heappop(scoville)
    if min1 >= K:
        return cnt
    else:
        return -1
    

scoville = [3, 4]
K = 7
print(solution(scoville, K))