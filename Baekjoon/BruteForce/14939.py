"""
백준 - https://www.acmicpc.net/problem/14939

< 불 끄기 >
"""

import sys

input = sys.stdin.readline
from itertools import product
import copy
board = [list(input().rstrip()) for _ in range(10)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]

answer = int(1e9)
switch = [0, 1] # 1이면 버튼 누르기
# 1행의 버튼들을 누르는 경우의 수
for lst in product(switch, repeat = 10):
    lights = copy.deepcopy(board) 
    count = 0
    # lst에 따라 1행의 버튼을 누르고 시작한다.
    for i in range(10):
        if lst[i] == 1:
            count += 1
            for dx, dy in direction:
                nx = dx
                ny = i + dy
                if 0 <= nx < 10 and 0 <= ny < 10:
                    if lights[nx][ny] == '#':
                        lights[nx][ny] = 'O'
                    else:
                        lights[nx][ny] = '#'

    # 2행부터 시작하여, 이전 행의 전구가 켜져있다면 버튼을 누르기
    for i in range(1, 10):
        for j in range(10):
            if lights[i - 1][j] == 'O':
                count += 1
                for dx, dy in direction:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < 10 and 0 <= ny < 10:
                        if lights[nx][ny] == '#':
                            lights[nx][ny] = 'O'
                        else:
                            lights[nx][ny] = '#'

    for i in range(10):
        if lights[-1][i] == 'O':
            break
    else:
        answer = min(answer, count)

if answer == int(1e9):
    print(-1)
else:
    print(answer)