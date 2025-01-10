"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/67256

< [카카오 인턴] 키패드 누르기 >
"""

from collections import defaultdict


def solution(numbers, hand):
    num = defaultdict(tuple)
    left, right = (3, 0), (3, 2)
    x, y = 0, 0
    for i in range(1, 10):
        num[i] = (x, y)
        y += 1
        if y == 3:
            y = 0
            x += 1
    num[0] = (3, 1)
    answer = ""
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            left = num[i]
        elif i in [3, 6, 9]:
            answer += "R"
            right = num[i]
        else:
            x, y = left
            x2, y2 = right
            a, b = num[i]
            dist = abs(x - a) + abs(y - b)
            dist2 = abs(x2 - a) + abs(y2 - b)

            if dist < dist2:
                answer += "L"
                left = num[i]
            elif dist == dist2:
                if hand == "left":
                    answer += "L"
                    left = num[i]
                else:
                    answer += "R"
                    right = num[i]
            else:
                answer += "R"
                right = num[i]
    return answer
