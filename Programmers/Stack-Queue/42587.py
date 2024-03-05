"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42587

< 프로세스 >
"""

from collections import deque


def solution(priorities, location):
    answer = 0
    num = [i for i in range(len(priorities))]
    lst = deque(zip(priorities, num))
    max_val = max(priorities)

    while True:
        x, y = lst.popleft()
        if x == max_val:
            priorities.remove(max_val)
            if len(priorities) != 0:
                max_val = max(priorities)
            answer += 1

            if y == location:
                break
        else:
            lst.append((x, y))

    return answer
