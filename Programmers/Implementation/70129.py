"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/70129

< 이진 변환 반복하기 >
"""


def solution(s):
    count = 0
    zero = 0
    while s != "1":
        zero += s.count("0")
        c = len(s.replace("0", ""))
        s = bin(c)[2:]
        count += 1

    return [count, zero]
