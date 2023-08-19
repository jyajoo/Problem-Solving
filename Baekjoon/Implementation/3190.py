"""
백준 - https://www.acmicpc.net/problem/3190

< 뱀 >
"""
import sys

input = sys.stdin.readline

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수

board = [[0] * n for _ in range(n)]
board[0][0] = 1  # 뱀의 몸 : 1, 몸 x : 0, 사과 : 2

# 상우하좌 (시계방향)
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

snake = []
a, b = 0, 0  # 뱀의 첫 시작 위치
d = 1  # da, db의 상우하좌 중, 우를 의미, 뱀의 초기 머리 방향
snake.append((0, 0))

# 사과의 위치 설정
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2

l = int(input())  # 방향 변환 횟수
time = 0  # 게임 시간

arr = []
breaker = False
# 방향 변환
for _ in range(l):
    x, c = input().split()
    arr.append((int(x), c))

x, c = arr.pop(0)
while True:
    a += da[d]
    b += db[d]
    time += 1
    snake.append((a, b))

    # 이동한 위치가 보드를 벗어나는지 확인
    if a < 0 or a >= len(board) or b < 0 or b >= len(board):
        break
    
    # 이동한 위치에 이미 뱀의 몸이 존재하는지 확인
    if board[a][b] == 1:
        break

    # 이동한 위치에 사과가 있는 경우
    if board[a][b] == 2:
        board[a][b] = 1
    
    # 이동한 위치에 사과가 없는 경우, 꼬리 부분 삭제
    else:
        board[a][b] = 1
        tail = snake.pop(0)
        board[tail[0]][tail[1]] = 0
    
    # time이 x초에 도달한 경우, 다음 방향으로 변환
    if time == x:
        if c == 'L':
            d -= 1
        else:
            d += 1
        
        if d == -1:
            d = 3
        elif d == 4:
            d = 0
        if len(arr) > 0:
            x, c = arr.pop(0)
print(time)