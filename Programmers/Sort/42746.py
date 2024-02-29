"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42746

< 가장 큰 수 >
"""

import functools


def comparator(a, b):
    if int(a + b) > int(b + a):
        return -1
    else:
        return 1


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=functools.cmp_to_key(comparator))
    return str(int("".join(numbers)))


"""
"""


def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int("".join(numbers)))

    return answer
