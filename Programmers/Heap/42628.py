"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42628#

< 이중 우선순위 큐 >
"""

import heapq


def solution(operations):
    number1 = []
    number2 = []
    for op in operations:
        c = op[0]
        num = int(op[1:])
        if c == "I":
            heapq.heappush(number1, num)  # 최소
            heapq.heappush(number2, -num)  # 최대
            continue

        if num == -1 and number1:
            x = heapq.heappop(number1)
            number2.remove(-x)

        elif num == 1 and number2:
            x = heapq.heappop(number2)
            number1.remove(-x)

    answer = []
    if not number1:
        answer = [0, 0]
    else:
        a = heapq.heappop(number1)
        b = -heapq.heappop(number2)
        answer = [b, a]
    return answer
