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

'''
- DP로 풀이 (바텀업)
'''
import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

# 메모이제이션 (무한대로 초기화)
dp = [float('inf')] * (n + 1)
dp[0] = 0

# 0부터 n까지 바텀업 방식
for i in range(n + 1):
    if i >= a:
        dp[i] = min(dp[i], dp[i - a] + 1)
    if i >= b:
        dp[i] = min(dp[i], dp[i - b] + 1)

if dp[n] != float('inf'):
    print(dp[n])
else:
    print(-1)

# print(dp[n] if dp[n] != float('inf') else -1)