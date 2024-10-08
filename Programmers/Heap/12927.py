'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12927

< 야근 지수 >
'''
import heapq

def solution(n, works):
    answer = 0
    if sum(works) - n <= 0:
        return 0
    
    works = [-i for i in works]
    heapq.heapify(works)
    
    for _ in range(n):
        max_val = -heapq.heappop(works)
        heapq.heappush(works, -(max_val - 1))
    
    for i in works:
        answer += i ** 2
    
    return answer