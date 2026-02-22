'''
백준 - https://www.acmicpc.net/problem/11726

< 2xn 타일링 >
'''
'''
1 <= n <= 1000
다이나믹 프로그래밍

n의 경우, n-1의 경우들에 ㅣ덧붙이기, n-2의 경우들에 (ㅡ, ㅡ) 가로 2줄 덧붙이기

dp[n] = dp[n - 1] + dp[n - 2]
'''
import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

if n <= 2:
    print(n)
else: 
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    print(dp[n])
