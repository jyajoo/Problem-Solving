"""
구름톤 챌린지 - https://level.goorm.io/exam/195695/%EB%B0%9C%EC%A0%84%EA%B8%B0-2/quiz/1

< 발전기 (2) >
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y, t):
    queue = deque()
    queue.append((x, y))
    count = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            # 마을 밖인 경우 + 건물 유형(t)이 다른 경우 + 이미 방문한 경우
            if (
                nx in (-1, n)
                or ny in (-1, n)
                or village[nx][ny] != t
                or visited[nx][ny]
            ):
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))
            count += 1

            if count == k:
                type[t] += 1


n, k = map(int, input().split())

village = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
type = {}
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if village[i][j] not in type:
                type[village[i][j]] = 0

            visited[i][j] = True
            bfs(i, j, village[i][j])

type = list(type.items())
type.sort(key=lambda x: (-x[1], -x[0]))
print(type)
print(type[0][0])

"""
- defaultdict 사용
"""
import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline


def bfs(x, y, t):
    queue = deque()
    queue.append((x, y))
    count = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            # 마을 밖인 경우 + 건물 유형(t)이 다른 경우 + 이미 방문한 경우
            if (
                nx in (-1, n)
                or ny in (-1, n)
                or village[nx][ny] != t
                or visited[nx][ny]
            ):
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))
            count += 1

            if count == k:
                type[t] += 1


n, k = map(int, input().split())

village = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
type = defaultdict(int)
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            type[village[i][j]]
            visited[i][j] = True
            bfs(i, j, village[i][j])

type = list(type.items())
type.sort(key=lambda x: (-x[1], -x[0]))
print(type)
print(type[0][0])
