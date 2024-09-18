'''
백준 - https://www.acmicpc.net/problem/26169

< 세 번 이내에 사과를 먹자 >
'''
from sys import stdin
input = stdin.readline

def backtracking(r, c, count, apple):
    global answer
    # 3번 이하의 이동으로 사과를 2개 이상 먹을 수 있는 경우
    if count <= 3 and apple >= 2:
        answer = 1
        return 

    for dx, dy in direction:
        nx = r + dx
        ny = c + dy
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        
        # 장애물이 없다면
        if board[nx][ny] != -1:
            a = board[nx][ny]
            board[nx][ny] = -1 # 즉시 장애물 처리
            # 사과가 있는 경우
            if a == 1: 
                backtracking(nx, ny, count + 1, apple + 1)
            else:
                backtracking(nx, ny, count + 1, apple)
            board[nx][ny] = a


# 1이면 사과, 0이면 빈칸, -1이면 장애물
board = [list(map(int, input().split())) for _ in range(5)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = map(int, input().split())

# 출발 부분에 사과가 있는지 확인
apple = 0
if board[r][c] == 1:
    apple += 1
board[r][c] = -1 # 장애물 처리
answer = 0
backtracking(r, c, 0, apple)
print(answer)