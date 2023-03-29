# 인접 행렬(Adjacency Matrix) (메모리 낭비)

INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)


# 인접 리스트(Adjacency List) (연결 정보 찾는 속도 느림)
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)


# dfs(스택)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = " ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    

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

visited = [False] * len(graph)
dfs(graph, 1, visited)   # 그래프, 최상단 노드, 방문체크