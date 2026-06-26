"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12953

< N개의 최소 공배수 >
"""

import math


def solution(arr):
    answer = math.lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        answer = math.lcm(answer, arr[i])

    return answer
