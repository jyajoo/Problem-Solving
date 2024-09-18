"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/181188

< 요격 시스템 >
"""


def solution(targets):
    answer = 1
    targets.sort(key=lambda x: x[1])

    now_e = targets[0][1] - 0.5
    for s, e in targets:
        if now_e < s or now_e > e:
            now_e = e - 0.5
            answer += 1

    return answer
