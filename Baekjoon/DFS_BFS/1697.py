'''
백준 - https://www.acmicpc.net/problem/1697

< 숨바꼭질 >
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    global visited
    q = deque()
    q.append((x, 0))
    visited[x] = 0

    while q:
        n, c = q.popleft()

        for nx in (n - 1, n + 1, n * 2):
            if nx >= 0 and nx < 100001 and visited[nx] > c + 1:
                visited[nx] = c + 1
                q.append((nx, c + 1))        

n, k = map(int, input().split())
visited = [int(1e9)] * 100001
bfs(n)
print(visited[k])