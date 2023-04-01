'''
< 음료수 얼려먹기 >
 
- BFS 풀이
'''

from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

x, y = 0, 0
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
while True:    
    queue = deque([x, y])
    arr[x][y] = '1'
    while queue:
        x, y = queue.popleft(), queue.popleft()
        for i in range(4):
            if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= m:
                continue
            if arr[x + dx[i]][y + dy[i]] != '1':
                queue.append(x + dx[i])
                queue.append(y + dy[i])
                arr[x + dx[i]][y + dy[i]] = '1'
    result += 1

    flag = False
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '0':
                x = i
                y = j
                flag = True
                break
        if flag:
            break
    if not flag:
        break

print(result)           

'''
- DFS 풀이
'''
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):    
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)