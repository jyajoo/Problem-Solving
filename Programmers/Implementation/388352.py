'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/388352

< 비밀 코드 해독 >
'''
from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    for i in list(combinations([i for i in range(1, n + 1)], 5)):
        for idx, j in enumerate(q):
            si = set(i)
            sj = set(j)
            if 5 -len(si - sj) != ans[idx]:
                break
        else:
            answer += 1
    
    
    return answer