"""
백준 - https://www.acmicpc.net/problem/2630

< 색종이 만들기 >
"""

import sys

input = sys.stdin.readline


def func(x, y, m):
    global white, blue
    check = board[x][y]
    flag = False
    for i in range(x, x + m):
        for j in range(y, y + m):
            if board[i][j] != check:
                flag = True
                break
        if flag:
            func(x, y, m // 2)
            func(x + m // 2, y, m // 2)
            func(x, y + m // 2, m // 2)
            func(x + m // 2, y + m // 2, m // 2)
            break
    else:
        if check == 1:
            blue += 1
        else:
            white += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0
func(0, 0, n)
print(white)
print(blue)
