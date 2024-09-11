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
