'''
백준 - https://www.acmicpc.net/problem/1058

< 친구 >

a가 b의 2-친구가 되기 위해
두 사람이 친구이거나
a의 친구이고 b와 친구인 c 필요

가장 유명한 사람은 2-친구의 수가 많은 사람
a와 b가 친구이면 b와 a도 친구고 a와 a는 친구 아님

n <= 50
'''
'''
플로이드워셜 알고리즘
- 모든 지점에서 모든 지점까지의 최단 경로 모두 구하는 알고리즘
'''
import sys

input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]
for i in range(n):
    a = input().strip()
    for j in range(n):
        if i == j:
            graph[i][j] = 0
        elif a[j] == 'N':
            graph[i][j] = int(1e9)
        else:
            graph[i][j] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in graph:
    count = 0
    for j in i:
        if 0 < j and j <= 2:
            count += 1
    result = max(result, count)
print(result)