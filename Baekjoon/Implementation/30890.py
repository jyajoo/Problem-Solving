"""
백준 - https://www.acmicpc.net/problem/30890

< 드럼 >
"""
import sys

input = sys.stdin.readline

x, y = map(int, input().split())


def gcd(x, y):
    while y:
        x, y = y, x % y

    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


LCM = lcm(x, y)
result = [0] * (LCM + 1)

for i in range(1, x + 1):
    result[(LCM // x) * i] = 1

for i in range(1, y + 1):
    m = (LCM // y) * i
    if result[m] == 1:
        result[m] = 3
    else:
        result[m] = 2

for i in result:
    if i != 0:
        print(i, end = "")