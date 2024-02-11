"""
백준 - https://www.acmicpc.net/problem/16234

< 인구 이동 >
"""
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    global visited
    q = deque()
    q.append((x, y))
    union = [(x, y)] # 연합
    sum_val = board[x][y] # 총합
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 인접하는 나라와의 인구 차이가 기준에 적합하다면, 연합에 추가한다.
                if l <= abs(board[x][y] - board[nx][ny]) <= r:
                    union.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    sum_val += board[nx][ny]

    # 연합에 포함된 나라 간의 인구 이동 
    if len(union) > 1:
        for x, y in union:
            board[x][y] = sum_val // len(union)
        return True


n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
count = 0
while True:
    flag = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 연합에 포함되지 않은 경우, bfs 탐색을 시도한다.
            # bfs를 통해 인구 이동이 진행되었다면, flag를 True로 표현하여 체크
            if not visited[i][j] and bfs(i, j):
                flag = True
    
    # 한 번이라도 인구 이동이 진행된 경우, count + 1
    if flag:
        count += 1
    else:
        break
print(count)
