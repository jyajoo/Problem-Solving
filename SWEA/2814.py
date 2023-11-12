"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GOPPaAeMDFAXB&categoryId=AV7GOPPaAeMDFAXB&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1#

< 최장 경로 >
"""
import sys

sys.stdin = open("C:\coding\github\Algorithm\SWEA\sample_input.txt", "r")


def dfs(v, count):
    global answer
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, count + 1)
    visited[v] = False
    answer = max(answer, count)


T = int(input())

for x in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N + 1)
    answer = 0
    count = 1
    for i in range(1, N + 1):
        dfs(i, count)

    print("#{} {}".format(x + 1, answer))
