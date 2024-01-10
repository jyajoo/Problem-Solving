"""
백준 - https://www.acmicpc.net/problem/11687

< 팩토리얼 0의 개수 >
"""
import sys

input = sys.stdin.readline


def find_zero(n):
    zero = 0
    while n != 0:
        zero += n // 5
        n //= 5

    return zero


m = int(input())

start = 1
end = m * 5
result = -1

while start <= end:
    middle = (start + end) // 2
    zero = find_zero(middle)

    if zero >= m:
        if zero == m:
            result = middle
        end = middle - 1
    else:
        start = middle + 1

print(result)
