"""
백준 - https://www.acmicpc.net/problem/2533

< 사회망 서비스(SNS) >
"""
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(now):
    visited[now] = True

    # 현재 노드가 얼리가 아니면 0개
    # 현재 노드가 얼리라면 1개로 설정
    dp[now][0] = 0
    dp[now][1] = 1

    # 자식 노드가 있는 경우,
    for child in graph[now]:
        if not visited[child]:
            dfs(child)
            dp[now][0] += dp[child][1]
            dp[now][1] += min(dp[child][0], dp[child][1])


# 정점의 개수
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# i번째 노드가 얼리 아답터이거나 아닐때(0, 1) 필요한 최소 얼리 아답터의 수
dp = [[0] * 2 for _ in range(n + 1)]
visited = [False] * (n + 1)
dfs(1)
print(min(dp[1]))
