'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12973

< 짝지어 제거하기 >
'''
from collections import deque
def solution(s):
    if len(s) % 2 != 0:
        return 0
    
    new = deque()
    prev = s[0]
    new.append(prev)
    for i in s[1:]:
        if i == prev:
            new.pop()
            if new:
                prev = new[-1]
            else:
                prev = '0'
        else:
            prev = i
            new.append(i)
    
    if new:
        return 0
    return 1