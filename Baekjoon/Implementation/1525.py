"""
백준 - https://www.acmicpc.net/problem/1525

< 퍼즐 >
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((puzzle))
    while q:
        p = q.popleft()
        count = visited[p]
        if p == "123456780":
            return count

        zero = p.index("0")
        x, y = zero // 3, zero % 3
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                p_list = list(p)
                p_list[x * 3 + y], p_list[nx * 3 + ny] = (
                    p_list[nx * 3 + ny],
                    p_list[x * 3 + y],
                )
                new_p = "".join(p_list)
                if visited.get(new_p) == None:
                    visited[new_p] = count + 1
                    q.append((new_p))
    return -1


puzzle = ""
for _ in range(3):
    a, b, c = input().split()
    puzzle += a + b + c


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = {puzzle: 0}
print(bfs())
