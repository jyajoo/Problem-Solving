"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/120812

< 최빈값 구하기 >
"""

from collections import Counter


def solution(array):
    frequency = Counter(array)

    max_v = max(frequency.values())
    answer = None

    for k, v in frequency.items():
        if v == max_v:
            if answer is None:
                answer = k
            else:
                return -1

    return answer
