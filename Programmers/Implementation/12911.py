"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12911

< 다음 큰 숫자 >
"""


def solution(n):
    count = format(n, "b").count("1")
    while True:
        n += 1
        if format(n, "b").count("1") == count:
            break
    return n
