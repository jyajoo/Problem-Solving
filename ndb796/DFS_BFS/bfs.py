from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visted[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visted[i]:
                visited[i] = True
                queue.append(i)

graph = [
    [],         # 노드 번호 1부터 시작
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visted = [False] * len(graph)
bfs(graph, 1, visted)