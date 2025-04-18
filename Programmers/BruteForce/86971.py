"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/86971

< 전력망을 둘로 나누기 >
"""

from collections import deque


def bfs(a, graph):
    q = deque()
    q.append(a)
    visited = [False] * len(graph)
    visited[a] = True
    count = 1
    while q:
        x = q.popleft()
        print(x, graph[x])
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1
    return count


def solution(n, wires):
    answer = int(1e9)

    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        c1 = bfs(a, graph)
        c2 = n - c1
        answer = min(answer, abs(c1 - c2))

        graph[a].append(b)
        graph[b].append(a)

    return answer
'''
'''
from collections import deque
def solution(n, wires):
    def bfs(a, b):
        visited = [False] * (n + 1)
        q = deque()
        q.append(a)
        visited[a] = True
        cnt = 0
        while q:
            a = q.popleft()
            cnt += 1
            for x in graph[a]:
                if not visited[x] and x != b:
                    visited[x] = True
                    q.append(x)
        return cnt
                
            
    answer = int(1e9)
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        cnt1 = bfs(a, b)
        cnt2 = bfs(b, a)
        answer = min(answer, abs(cnt1 - cnt2))
    
    
    return answer