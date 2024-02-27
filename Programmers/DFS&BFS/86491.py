"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/86491

< 최소 직사각형 >
"""

def solution(sizes):
    for i, [x, y] in enumerate(sizes):
        if x > y:
            sizes[i] = [y, x]
    w, h = 0, 0
    for x, y in sizes:
        w = max(w, x)
        h = max(h, y)
    return w * h
