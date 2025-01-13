"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/17682

< [1차] 다트 게임 >
"""


def solution(dartResult):
    arr = []
    score = 0
    for idx, i in enumerate(dartResult):
        if i.isdigit() and dartResult[idx - 1].isdigit():
            score = score * 10 + int(i)
        elif i.isdigit():
            arr.append(score)
            score = int(i)
        elif i == "S":
            score = score**1
        elif i == "D":
            score = score**2
        elif i == "T":
            score = score**3
        elif i == "*":
            score *= 2
            if len(arr) != 0:
                arr[-1] *= 2
        elif i == "#":
            score = -score
    arr.append(score)
    print(arr)
    return sum(arr)
