"""
백준 - https://www.acmicpc.net/problem/1676

< 팩토리얼 0의 개수 >
"""
import sys
import math
input = sys.stdin.readline

n = int(input())
num = str(math.factorial(n))

result = 0
for i in range(len(num) - 1, -1, -1):
    if num[i] != '0':
        break
    result += 1

print(result)

