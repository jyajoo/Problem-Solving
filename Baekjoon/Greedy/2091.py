"""
백준 - https://www.acmicpc.net/problem/2091

< 동전 >
"""
import sys

input = sys.stdin.readline

x, a, b, c, d = map(int, input().split())
unit_index = {1: 0, 5: 1, 10: 2, 25: 3}
unit_coins = {1: a, 5: b, 10: c, 25: d}
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


result = dp[x][:4]

if dp[x][0] == -1:
    result = [0] * 4

print(*result)

"""
"""
import sys

input = sys.stdin.readline
import copy

x, a, b, c, d = map(int, input().split())
total_money = a + 5 * b + 10 * c + 25 * d
coins_count = [(1, a), (5, b), (10, c), (25, d)]

min_count = int(1e9)
min_coins = [0] * 4
for i in range(d + 1):
    money = total_money - 25 * i
    coins = [0] * 4
    coins[3] = i

    # 10, 5, 1의 순서로 동전이 최소가 되도록 빼준다
    for j in [2, 1, 0]:
        unit, coin_count = coins_count[j]
        for c in range(coin_count, -1, -1):
            if money - unit * c >= x:
                money -= unit * c
                coins[j] = c
                break

    if money == x and sum(coins) < min_count:
        min_count = sum(coins)
        min_coins = copy.deepcopy(coins)

answer = [0] * 4

if min_count != int(1e9):
    for i in range(4):
        _, c = coins_count[i]
        answer[i] = c - min_coins[i]

print(*answer)
"""
"""
import sys

input = sys.stdin.readline
import copy

x, a, b, c, d = map(int, input().split())
total_money = a + 5 * b + 10 * c + 25 * d
coins_count = [(1, a), (5, b), (10, c), (25, d)]

min_count = int(1e9)
min_coins = [0] * 4
for i in range(d + 1):
    money = total_money - 25 * i
    coins = [0] * 4
    coins[3] = i

    k = money - x # 최소의 동전으로 k원 만들기
    if k < 0:
        continue
    # 10, 5, 1의 순서로 동전이 최소가 되도록 빼준다
    for j in [2, 1, 0]:
        unit, coin_count = coins_count[j]
        count = k // unit
        if count > coin_count:
            count = coin_count
        k = k - count * unit
        coins[j] = count
        if k == 0 and sum(coins) < min_count:
            min_count = sum(coins)
            min_coins = copy.deepcopy(coins)
            break

answer = [0] * 4

if min_count != int(1e9):
    for i in range(4):
        _, c = coins_count[i]
        answer[i] = c - min_coins[i]

print(*answer)
