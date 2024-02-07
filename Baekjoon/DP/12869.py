"""
백준 - https://www.acmicpc.net/problem/12869

< 뮤탈리스크 >
"""
import sys
input = sys.stdin.readline
from itertools import permutations

def dfs(i, j, k, count):
    global answer
    if i <= 0 and j <= 0 and k <= 0:
        answer = min(answer, count)
        return 
    
    if i < 0:
        i = 0
    if j < 0:
        j = 0
    if k < 0:
        k = 0

    if dp[i][j][k] <= count:
        return
    dp[i][j][k] = min(dp[i][j][k], count)

    for a, b, c in attacks:
        dfs(i - a, j - b, k - c, count + 1)        

n = int(input())
lst = list(map(int, input().split()))

# 뮤탈리스크를 공격하는 경우의 수
attack = [9, 3, 1]
attacks = list(permutations(attack, 3))

# dp[scv1][scv2][scv3] : 각 scv가 해당 체력일 때의 최소 공격 횟수를 의미한다.
dp = [[[int(1e9)] * 61 for _ in range(61)] for _ in range(61)]

# n이 3보다 작다면, 체력이 0인 scv 추가
if n < 3:
    for _ in range(3 - n):
        lst += [0]

answer = int(1e9)
dfs(lst[0], lst[1], lst[2], 0)
print(answer)