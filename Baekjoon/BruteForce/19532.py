"""
백준 - https://www.acmicpc.net/problem/19532

< 수학은 비대면강의입니다 >
"""
import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
for i in range(-999, 1000):
    flag = False
    for j in range(-999, 1000):
        if a * i + b * j == c and d * i + e * j == f:
            flag = True
            print(i, j)

    if flag:
        break
