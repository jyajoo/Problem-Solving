"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/120808

< 분수의 덧셈 >
"""


def solution(numer1, denom1, numer2, denom2):
    answer = []

    # 최소 공배수
    denom = max(denom1, denom2)
    while True:
        if denom % denom1 == 0 and denom % denom2 == 0:
            break
        denom += 1

    numer1 *= denom // denom1
    numer2 *= denom // denom2
    numer = numer1 + numer2

    # 최대 공약수
    num = max(numer, denom)
    while True:
        if numer % num == 0 and denom % num == 0:
            break
        num -= 1
        if num == 1:
            break

    return [numer // num, denom // num]


"""
"""
import math


def solution(numer1, denom1, numer2, denom2):

    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1

    gcd = math.gcd(denom, numer)

    return [numer // gcd, denom // gcd]
