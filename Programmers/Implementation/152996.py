"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/152996

< 시소 짝궁 >
"""

from collections import Counter


def find(a, b):
    for i in [2, 3, 4]:
        for j in [2, 3, 4]:
            if a * i == b * j:
                return True
    return False


def solution(weights):
    answer = 0
    w = Counter(weights)
    weights = list(set(weights))
    weights.sort()

    for i in range(len(weights)):
        a = weights[i]
        if w[a] > 1:
            answer += w[a] * (w[a] - 1) // 2

        for j in range(i + 1, len(weights)):
            b = weights[j]
            if find(a, b):
                answer += w[a] * w[b]

    return answer
'''
'''
from itertools import combinations
from collections import Counter

def solution(weights):
    answer = 0
    counter = dict(Counter(weights))
    weights = list(counter.keys())
    weights.sort()

    for i in counter.values():
        if i > 1:
            answer += (i * (i - 1)) / 2
    
    for (a, b) in combinations(weights, 2):
        if a * 4 == b * 2 or a * 3 == b * 2 or a * 4 == b * 3:
                answer += counter[a] * counter[b]
    return answer