"""
백준 - https://www.acmicpc.net/problem/2231

< 분해합 >
"""
import sys

input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(n):
    num = str(i)
    result = i
    for j in num:
        result += int(j)
    
    if result == n:
        answer = i
        break

print(answer)