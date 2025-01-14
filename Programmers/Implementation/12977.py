"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12977

< 소수 만들기 >
"""

from itertools import combinations


def solution(nums):
    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    answer = 0
    for a, b, c in combinations(nums, 3):
        n = sum([a, b, c])
        if is_prime(n):
            answer += 1

    return answer
