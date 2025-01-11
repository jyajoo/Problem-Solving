"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/118666

< 성격 유형 검사하기 >
"""


def solution(survey, choices):
    score = {"A": 0, "N": 0, "C": 0, "F": 0, "M": 0, "J": 0, "R": 0, "T": 0}
    for sur, cho in zip(survey, choices):
        a, b = sur[0], sur[1]
        if cho < 4:
            score[a] += 4 - cho
        elif cho > 4:
            score[b] += cho - 4

    answer = ""
    for a, b in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        if score[a] < score[b]:
            answer += b
        else:
            answer += a
    return answer
