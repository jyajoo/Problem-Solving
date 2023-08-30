"""
구름톤 챌린지 - https://level.goorm.io/exam/195694/%EB%B0%9C%EC%A0%84%EA%B8%B0/quiz/1\

< 발전기 >
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
village = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

queue = deque()
visited = [[False] * (n) for _ in range(n)]

result = 0
for a in range(n):
    for b in range(n):
        # 집이 있다면
        if village[a][b] == 1 and not visited[a][b]:
            visited[a][b] = True
            result += 1
            queue.append((a, b))
            while queue:
                x, y = queue.popleft()
                # 상하좌우 체크
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    # 마을을 벗어난다면, 넘어간다
                    if nx > 0 and nx < n and ny >= 0 and ny < n:
                        # 상하좌우에 집이 있고, 방문한 적이 없다면
                        if village[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

                    # # 마을을 벗어난다면, 넘어간다
                    # if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    #     continue

                    # # 상하좌우에 집이 있고, 방문한 적이 없다면
                    # if village[nx][ny] == 1 and not visited[nx][ny]:
                    #     visited[nx][ny] = True
                    #     queue.append((nx, ny))

print(result)

"""
"""
import sys

input = sys.stdin.readline


def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    while stack:
        x, y = stack.pop()

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            # 마을을 벗어난 경우 + 집이 아닌 경우 + 이미 방문한 경우
            if (
                nx in (-1, n)
                or ny in (-1, n)
                or village[nx][ny] == 0
                or visited[nx][ny]
            ):
                continue

            visited[nx][ny] = True
            stack.append((nx, ny))


n = int(input())
village = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

visited = [[False] * (n) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(n):
        # 방문하지 않은 집이 있다면 탐색 시작
        if village[i][j] and not visited[i][j]:
            result += 1
            dfs(i, j)
print(result)
