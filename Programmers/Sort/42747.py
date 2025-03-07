''' 
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42747

< H-Index >
'''
def solution(citations):
    answer = 0
    citations.sort(key = lambda x : -x)
    for i in range(len(citations) + 1):
        if i == len(citations):
            answer = i
            break
        if citations[i] <= i:
            answer = i
            break
    return answer

'''
'''
from collections import Counter

def solution(citations):
    citations.sort(reverse = True)
    counts = dict(Counter(citations))
    for h in range(len(citations), 0, -1):   
        x, y = 0, 0
        
        for k, v in counts.items():
            if k >= h:
                x += v
            if k <= h:
                y += v
        if x >= h and y <= h:
            return h
    return 0
'''
'''
def solution(citations):
    n = len(citations)
    for h in range(max(citations), -1, -1):
        count, count2 = 0, 0
        for i in citations:
            if i >= h:
                count += 1
            else:
                count2 += 1
        if count >= h and count2 <= h:
            return h
    return 0