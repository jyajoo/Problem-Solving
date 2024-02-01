"""
백준 - https://www.acmicpc.net/problem/5546

< 파스타 >
"""
import sys

input = sys.stdin.readline

MOD = 10000
n, k = map(int, input().split())

# 현재 몇 일차의 파스타를 선택할 것인지
# 어떤 파스타 종류를 선택할 것인지
# 해당 파스타가 연속적으로 몇 번 선택되었는지
# 를 모두 고려하여서 현재의 파스타를 선택하여야 한다.
dp = [[[0, 0, 0] for _ in range(4)] for _ in range(n + 1)]
pasta = [0] * (n + 1)
for _ in range(k):
    a, b = map(int, input().split())
    pasta[a] = b

if pasta[1] != 0:
    dp[1][pasta[1]][1] = 1
else:
    dp[1][1][1] = 1
    dp[1][2][1] = 1
    dp[1][3][1] = 1

for i in range(2, n + 1):
    for x in range(1, 4):
        # 파스타가 지정된 날이지만, 해당 파스타가 아닌 경우 넘어간다
        # 파스타가 지정되어, 해당 파스타 종류에 해당할 경우에만 실행하도록 한다
        if pasta[i] != 0 and x != pasta[i]:
            continue
        for y in range(1, 4):
            # 연속적으로 동일한 파스타를 고를 경우
            # 전날의 해당 파스타의 경우의 수와 똑같다.
            if x == y:
                dp[i][x][2] = dp[i - 1][y][1]
            
            # 전날의 파스타와 "다른 종류"를 선택하는 경우
            # 전날의 다른 종류의 파스타가 선택되는 모든 경우의 수를 합한 것과 똑같다.
            else:
                dp[i][x][1] += dp[i - 1][y][1] + dp[i - 1][y][2]
                dp[i][x][1] %= MOD

print((sum(dp[n][1]) + sum(dp[n][2]) + sum(dp[n][3])) % MOD)