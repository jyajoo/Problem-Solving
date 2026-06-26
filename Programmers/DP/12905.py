'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12905

< 가장 큰 정사각형 찾기 >
'''
def solution(board):
    answer = 0
    w, h = len(board), len(board[0])
    for i in range(w):
        for j in range(h):
            if board[i][j]:
                if i > 0 and j > 0:
                    board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
                answer = max(answer, board[i][j] ** 2)

    return answer