'''
구름톤 챌린지 - https://level.goorm.io/exam/195702/%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0/quiz/1

< 연결 요소 제거하기 >
'''

import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

n, k, q = map(int, input().split())
arr = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(n):
    arr.append(list(input().rstrip()))

for _ in range(q):
    y, x, d = input().split()
    arr[int(y) - 1][int(x) - 1] = d
    visited = [[False for _ in range(n)] for _ in range(n)]
    alpha = defaultdict(int)

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                e = arr[i][j]
                alpha[e] += 1
                queue = deque()
                queue.append((i, j))
                mapping = [(i, j)]
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if (nx >= 0 and nx < n 
                        and ny >= 0 and ny < n 
                        and arr[nx][ny] == e 
                        and not visited[nx][ny]):
                            visited[nx][ny] = True
                            alpha[e] += 1
                            queue.append((nx, ny))
                            mapping.append((nx, ny))
                
                if alpha[e] >= k:
                    for a, b in mapping:
                        arr[a][b] = '.'
                alpha[e] = 0

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = "")
    print()

