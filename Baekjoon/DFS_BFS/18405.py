"""
백준 - https://www.acmicpc.net/problem/18405

< 경쟁적 전염 >
"""
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
virus = []

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus.append((arr[i][j], 0, i, j))

virus.sort()

q = deque(virus)
time = 0
while q:
    v, t, a, b = q.popleft()
    if t == s:
        break
    for dx, dy in direction:
        na = a + dx
        nb = b + dy
        if na >= 0 and na < n and nb >= 0 and nb < n:
            if arr[na][nb] == 0:
                arr[na][nb] = v
                q.append((v, t + 1, na, nb))

print(arr[x - 1][y - 1])

"""
"""
import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
virus = defaultdict(list)
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus[arr[i][j]].append((i, j, 0))

keys = sorted(virus.keys())
q = deque()
for key in keys:
    for value in virus[key]:
        q.append(value)

while q:
    a, b, t = q.popleft()
    if t == s:
        break
    for dx, dy in direction:
        na = a + dx
        nb = b + dy
        if na >= 0 and na < n and nb >= 0 and nb < n:
            if arr[na][nb] == 0:
                arr[na][nb] = arr[a][b]
                q.append((na, nb, t + 1))

print(arr[x - 1][y - 1])
