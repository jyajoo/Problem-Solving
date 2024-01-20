"""
백준 - https://www.acmicpc.net/problem/14503

< 로봇 청소기 >
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

answer = 0
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    # 1. 현재 칸이 청소되지 않은 경우, 현재 칸을 청소한다.
    if room[r][c] == 0:
        room[r][c] = 2
        answer += 1

    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    for dx, dy in direction:
        nx = r + dx
        ny = c + dy
        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            # 1. 반시계 방향으로 회전한다.
            d = (d - 1) % 4 if d - 1 >= 0 else 3
            # 2. 바라보는 방향을 기준으로 앞칸이 청소되지 않은 경우, 한 칸 전진한다.
            x, y = direction[d]
            if room[r + x][c + y] == 0:
                r += x
                c += y
            break

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
        # 1. 후진할 수 있다면, 후진하고 1번으로
        reverse_d = (d + 2) % 4
        x, y = direction[reverse_d]
        if room[r + x][c + y] != 1:
            r += x
            c += y
        else:
            break

print(answer)
