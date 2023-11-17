'''
구름톤 챌린지 - https://level.goorm.io/exam/195702/%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0/quiz/1

< 연결 요소 제거하기 >
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x, d):
    arr[y][x] = d
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((y, x))
    count = 0
    while queue:
        y, x = queue.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            count += 1

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if (ny >= 0 and ny < n and nx >= 0 and nx < n 
            and arr[ny][nx] == arr[y][x]
            and not visited[ny][nx]):
                queue.append((ny, nx))
        
    if count >= k:
        count = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    arr[i][j] = "."

n, k, q = map(int, input().split())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
arr= [list(input()) for _ in range(n)]

for _ in range(q):
    y, x, d = input().split()
    bfs(int(y) - 1, int(x) - 1, d)


for i in range(n):
    for j in range(n):
        print(arr[i][j], end = "")
    print()

'''
'''
import sys
input = sys.stdin.readline

def dfs(y, x, d):
    arr[y][x] = d
    stack = [(y, x)]
    visited = set()

    while stack:
        y, x = stack.pop()
        if (y, x) not in visited:
            visited.add((y, x))
        
            for dy, dx in direction:
                ny, nx = y + dy, x + dx

                if ny >= 0 and ny < n and nx >= 0 and nx < n:
                    if arr[ny][nx] == arr[y][x]:
                        stack.append((ny, nx))
            
            if len(visited) >= k:
                for y, x in visited:
                    arr[y][x] = "."
                

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, k, q = map(int, input().split())
arr = [list(input()) for _ in range(n)]

for _ in range(q):
    y, x, d = input().split()
    dfs(int(y) - 1, int(x) - 1, d)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = "")
    print()