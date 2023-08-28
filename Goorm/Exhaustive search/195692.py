"""
구름톤 챌린지 - https://level.goorm.io/exam/195692/gamejam/quiz/1

< GameJam>
"""
import sys

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
    # count, command = "", ""
    # for i in info[a][b]:
    #     if str.isdigit(i):
    #         count += i
    #     else:
    #         command += i

    # count = int(count)
    count, command = int(info[a][b][:-1]), info[a][b][-1]
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
    count, command = int(info[x][y][:-1]), info[x][y][-1]
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

"""
"""
import sys


def play(y, x, n):
    visited = [[0] * n for _ in range(n)]
    visited[y][x] = 1

    notEnd = True

    while notEnd:
        dy, dx = command[y][x]
        for _ in range(count[y][x]):
            y = (y + dy) % n
            x = (x + dx) % n

            if visited[y][x]:
                notEnd = False
                break
            visited[y][x] = 1
    return sum([sum(i) for i in visited])


n = int(input())

# 구름이의 말 위치
a, b = map(int, input().split())
a, b = a - 1, b - 1

# 플레이어의 말 위치
x, y = map(int, input().split())
x, y = x - 1, y - 1

# 이동 정보
info = [list(input().split()) for _ in range(n)]

count = [[0] * n for _ in range(n)]
command = [[None] * n for _ in range(n)]
direction = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D": [1, 0]}

for i in range(n):
    for j in range(n):
        temp = info[i][j]
        count[i][j] = int(temp[:-1])
        command[i][j] = direction[temp[-1]]

scoreG = play(a, b, n)
scoreP = play(x, y, n)

if scoreG > scoreP:
    print("goorm", scoreG)
else:
    print("player", scoreP)
"""
"""
import sys


def play(x, y):
    notEnd = True
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    while notEnd:
        count, command = int(info[x][y][:-1]), info[x][y][-1]
        dx, dy = direction[command]
        for _ in range(count):
            x = (x + dx) % n
            y = (y + dy) % n
            if visited[x][y]:
                notEnd = False
                break
            visited[x][y] = True
    return sum([sum(i) for i in visited])


n = int(input())

# 구름이의 말 위치
Rg, Cg = map(int, input().split())
# 플레이어의 말 위치
Rp, Cp = map(int, input().split())
Rg, Cg, Rp, Cp = Rg - 1, Cg - 1, Rp - 1, Cp - 1

# 이동 정보
info = [list(input().split()) for _ in range(n)]

# 상하좌우
direction = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}

goorm = play(Rg, Cg)
player = play(Rp, Cp)

if goorm > player:
    print("goorm", goorm)
else:
    print("player", player)
