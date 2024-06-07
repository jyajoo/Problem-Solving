"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/250125

< [PCCE 기출문제] 9번 / 이웃한 칸 >
"""


def solution(board, h, w):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    color = board[h][w]
    count = 0
    for dx, dy in direction:
        nx = h + dx
        ny = w + dy
        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
            continue

        if board[nx][ny] == color:
            count += 1

    return count
