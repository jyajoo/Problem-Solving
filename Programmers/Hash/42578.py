"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42578

< 의상 >
"""

# 시간초과
from itertools import combinations
from math import prod


def solution(clothes):
    answer = 0
    wear = {}
    for i, j in clothes:
        if j not in wear:
            wear[j] = 1
        else:
            wear[j] += 1
    wear = list(wear.values())
    for i in range(1, len(wear) + 1):
        for j in combinations(wear, i):
            answer += prod(j)
    return answer


# 정답
def solution(clothes):
    answer = 1
    wear = {}
    for i, j in clothes:
        if j not in wear:
            wear[j] = 1
        else:
            wear[j] += 1
    wear = list(wear.values())

    for i in wear:
        answer *= i + 1
    return answer - 1
