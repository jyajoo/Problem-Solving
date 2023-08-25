"""
구름톤 챌린지 - https://level.goorm.io/exam/195692/gamejam/quiz/1

< GameJam>
"""
import sys
import re

input = sys.stdin.readline

n = int(input())  # 격자 보드 크기

# 구름과 플레이어의 보드
board_g = [[0] * n for _ in range(n)]
board_p = [[0] * n for _ in range(n)]

# 구름이의 말 위치
a, b = map(int, input().split())
a, b = a - 1, b - 1
board_g[a][b] = 1

# 플레이어의 말 위치
x, y = map(int, input().split())
x, y = x - 1, y - 1
board_p[x][y] = 1

# 점수
goorm, player = 1, 1

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이동 정보
info = []
for _ in range(n):
    info.append(list(input().split()))

breaker = False

# 구름 계산
while not breaker:
    count, command = "", ""
    for i in info[a][b]:
        if str.isdigit(i):
            count += i
        else:
            command += i

    count = int(count)
    index = {"U": 0, "D": 1, "L": 2, "R": 3}.get(command)
    for _ in range(count):
        a = (a + dx[index]) % n
        b = (b + dy[index]) % n

        if board_g[a][b] == 1:
            breaker = True
            break
        else:
            goorm += 1
            board_g[a][b] = 1
    if breaker:
        break

breaker = False

# 플레이어 계산
while not breaker:
    count, command = "", ""
    for i in info[x][y]:
        if str.isdigit(i):
            count += i
        else:
            command += i

    count = int(count)
    index = {"U": 0, "D": 1, "L": 2, "R": 3}.get(command)
    for _ in range(count):
        x = (x + dx[index]) % n
        y = (y + dy[index]) % n

        if board_p[x][y] == 1:
            breaker = True
            break
        else:
            player += 1
            board_p[x][y] = 1

if player > goorm:
    print("player", player)
else:
    print("goorm", goorm)
