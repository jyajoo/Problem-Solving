'''
구름톤 챌린지 - https://level.goorm.io/exam/195689/%EA%B5%AC%EB%A6%84-%EC%B0%BE%EA%B8%B0-%EA%B9%83%EB%B0%9C/quiz/1

< 구름 찾기 깃발 >
'''
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 시계방향
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
result = []
for a in range(n):
    for b in range(n):
        count = 0
        if board[a][b] == 1:
            continue
        for i in range(8):
            na = a + dx[i]
            nb = b + dy[i]
            if na >= 0 and na < n and nb >= 0 and nb < n:
                if board[na][nb] == 1:
                    count += 1
        result.append(count)

print(result.count(k))