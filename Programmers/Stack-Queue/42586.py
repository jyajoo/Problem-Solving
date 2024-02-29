"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42586

< 기능 개발 >
"""


def solution(progresses, speeds):
    answer = []

    prev = -1
    for i, p in enumerate(progresses):
        day = (100 - p) / speeds[i]

        if day > (100 - p) // speeds[i]:
            day = (100 - p) // speeds[i] + 1

        if prev >= day:
            answer[-1] += 1
        else:
            answer.append(1)
            prev = day

    return answer
