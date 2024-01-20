"""
백준 - https://www.acmicpc.net/problem/21316

< 스피카 >
"""
import sys

input = sys.stdin.readline

graph = [[] for _ in range(13)]

for i in range(12):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(1, 13):
    # 연결된 별이 3개이어야 한다.
    if len(graph[i]) == 3:
        count = []
        for j in graph[i]:
            count.append(len(graph[j]))

        count.sort()
        # 그리고 그 3개의 연결된 별에 연결된 개수가 각각 1,2,3개여야 한다
        if count == [1, 2, 3]:
            result = i
            break

print(result)
