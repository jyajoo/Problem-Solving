"""
구름톤 챌린지 - https://level.goorm.io/exam/195691/%ED%8F%AD%ED%83%84-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-2/quiz/1

< 폭탄 구현하기 (2) >
"""
import sys

input = sys.stdin.readline

# 상하좌우중
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]

n, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input().split()))

board_score = [[0] * n for _ in range(n)]
result = 0
for _ in range(k):
    x, y = map(int, input().split())
    for i in range(5):
        nx = x + dx[i] - 1
        ny = y + dy[i] - 1
        # board 밖이거나 #인 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        elif board[nx][ny] == "#":
            continue
        elif board[nx][ny] == "0":
            board_score[nx][ny] += 1
        elif board[nx][ny] == "@":
            board_score[nx][ny] += 2

        result = max(result, board_score[nx][ny])
print(result)
