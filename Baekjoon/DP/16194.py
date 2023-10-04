'''
백준 - https://www.acmicpc.net/problem/16194

< 카드 구매하기 2 >
'''
import sys
input = sys.stdin.readline

n = int(input())
card = [0] + list(map(int, input().split()))
dp = [int(1e9)] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + card[j])
    
print(dp[-1])