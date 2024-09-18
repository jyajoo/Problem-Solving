"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/250121

< [PCCE 기출문제] 10번 / 데이터 분석 >
"""


def solution(data, ext, val_ext, sort_by):
    new_data = []
    if ext == "code":
        i = 0
    elif ext == "date":
        i = 1
    elif ext == "maximum":
        i = 2
    else:
        i = 3

    for d in data:
        if d[i] < val_ext:
            new_data.append(d)

    if sort_by == "code":
        j = 0
    elif sort_by == "date":
        j = 1
    elif sort_by == "maximum":
        j = 2
    else:
        j = 3

    new_data.sort(key=lambda x: x[j])
    return new_data
