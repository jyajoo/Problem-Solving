"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12978
"""

import heapq


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    distance = [int(1e9)] * (N + 1)
    distance[1] = 0

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            for b, c in graph[now]:
                cost = dist + c
                if distance[b] > cost:
                    distance[b] = cost
                    heapq.heappush(q, (cost, b))

    dijkstra(1)
    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1

    return answer
