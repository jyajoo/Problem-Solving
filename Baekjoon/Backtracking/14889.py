"""
백준 - https://www.acmicpc.net/problem/14889

< 스타트와 링크 >
"""
import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
numbers = list(range(n))
answer = sys.maxsize

for team in combinations(numbers, n // 2):
    start = link = 0
    team2 = list(set(numbers) - set(team))

    for i, j in combinations(team, 2):
        start += arr[i][j] + arr[j][i]

    for i, j in combinations(team2, 2):
        link += arr[i][j] + arr[j][i]

    answer = min(answer, abs(start - link))

print(answer)

"""
"""
import sys


def dfs(team, x):
    global answer
    if len(team) == n // 2:
        start = link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]

        answer = min(answer, abs(start - link))
        return

    for i in range(x, n):
        if not visited[i]:
            visited[i] = True
            dfs(team + [i], i)
            visited[i] = False


input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
numbers = list(range(n))
answer = sys.maxsize
visited = [False] * n
dfs([], 0)
print(answer)
