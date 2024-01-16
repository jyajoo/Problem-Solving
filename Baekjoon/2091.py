"""
백준 - https://www.acmicpc.net/problem/2091

< 동전 >
"""
import sys

input = sys.stdin.readline

x, a, b, c, d = map(int, input().split())
unit_index = {1 : 0, 5 : 1, 10 : 2, 25 : 3}
unit_coins = {1 : a, 5 : b, 10 : c, 25 : d}
# dp[i][j] = i원일 때, j는 동전 개수(각 단위의 동전 개수 + 총 동전 개수)
dp = [[-1] * 5 for _ in range(x + 1)]
for i in range(5):
    dp[0][i] = 0

for i in range(1, x + 1):
    max_count = 0
    unit = 0
    for j in unit_index.keys():
        index = unit_index[j]
        if 0 <= i - j <= x:
            # i - j원일 때, j의 개수가 주어진 개수보다 적다면, 추가가능
            # i - j원일 때, 총 동전 개수 + 1이 가장 많아지는 단위를 찾기
            if dp[i - j][index] < unit_coins[j] and dp[i - j][-1] >= max_count:
                max_count = dp[i - j][-1]
                unit = j

    # 반영해주기
    if unit != 0:
        index = unit_index[unit]
        for n in range(5):
            dp[i][n] = dp[i - unit][n]
        dp[i][index] += 1
        dp[i][-1] += 1
                

result = [0] * 4
money = 0
index = 0
for unit in unit_index.keys():
    money += dp[x][index] * unit
    index += 1

if money == x:
    result = dp[x][:4]

print(*result)