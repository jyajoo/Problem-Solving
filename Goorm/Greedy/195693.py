"""
구름톤 챌린지 - https://level.goorm.io/exam/195693/%ED%86%B5%EC%A6%9D-2/quiz/1

< 통증 (2) >
"""
import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
result = 0
for i in range(n):
    if n % b == 0:
        result += n // b
        n %= b
        break
    if n < a:
        break
    n -= a
    result += 1

if n != 0:
    print(-1)
else:
    print(result)
