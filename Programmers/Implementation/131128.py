"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/131128

< 숫자 짝꿍 >
"""

from collections import Counter


def solution(X, Y):
    arr = []

    x = Counter(X)
    y = Counter(Y)

    for a, b in x.items():
        if a in y:
            arr += [a] * min(b, y[a])
    arr.sort(reverse=True)
    if len(arr) == 0:
        return "-1"
    elif arr[0] == "0":
        return "0"
    else:
        return "".join(arr)
