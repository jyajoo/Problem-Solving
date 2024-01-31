"""
백준 - https://www.acmicpc.net/problem/1398

< 동전 문제 >
"""
import sys

input = sys.stdin.readline

t = int(input())

dp = [int(1e9)] * 100
dp[0] = 0
for i in range(1, 100):
    for j in [1, 10, 25]:
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + 1)

for _ in range(t):
    n = int(input())
    result = 0
    
    while True:
        if n == 0:
            break
        result += dp[n % 100]
        n //= 100
    print(result)

'''
- 그리디
'''
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    result = 0

    while True:
        if n == 0:
            break

        count = int(1e9)
        # 25를 가질 수 있는 모든 경우의 수 체크
        for i in range(n % 100 // 25 + 1):
            val = n % 100
            val -= 25 * i
            x = i

            # 그리디
            for j in [10, 1]:
                x += val // j
                val %= j
            count = min(count, x)

        result += count
        n //= 100
    print(result)