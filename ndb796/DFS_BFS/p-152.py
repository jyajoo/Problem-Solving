'''
< 미로 탈출 >
'''
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

x, y = 0, 0
queue = deque([0, 0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
while queue:
    result += 1
    x = queue.popleft()
    y = queue.popleft()
    graph[x][y] = 0
    flag = True
    if x == n - 1 and y == m - 1:
        break
    for i in range(4):
        if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= m:
            continue
        if graph[x + dx[i]][y + dy[i]] == 1:
            queue.append(x + dx[i])
            queue.append(y + dy[i])
            graph[x + dx[i]][y + dy[i]] = 0
            flag = False
    if flag:
        result -= 1


print(result)

'''
5 6
101010
111111
000001
111111
111111
'''