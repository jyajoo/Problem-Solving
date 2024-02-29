"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42839

< 소수 찾기 >
"""

from itertools import permutations


def check(x):
    if x <= 1:
        return False
    if x == 2:
        return True

    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    numbers = list(numbers)

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            n = int("".join(j))
            if check(n):
                answer.add(n)

    return len(answer)
