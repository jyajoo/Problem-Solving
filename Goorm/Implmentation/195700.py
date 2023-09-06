"""
구름톤 챌린지 - https://level.goorm.io/exam/195700/%EC%A4%91%EC%B2%A9-%EC%A0%90/quiz/1

< 중첩 점 >
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
box = [[[0, 0] for _ in range(n)] for _ in range(n)]

direction = {'U' : (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
for _ in range(m):
    y, x, d = input().split()
    y, x = int(y) - 1, int(x) - 1
    dy, dx = direction.get(d)
    while y >= 0 and y < n and x >= 0 and x < n:
        if d == 'U' or d == 'D':
            box[y][x][0] += 1
        else:
            box[y][x][1] += 1

        y += dy
        x += dx
result = 0
for i in range(n):
    for j in range(n):
        result += box[i][j][0] * box[i][j][1]
print(result)
