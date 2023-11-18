"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

< [S/W 문제해결 기본] 5일차 - Magnetic >
"""
import sys

sys.stdin = open("C:\coding\github\Algorithm\SWEA\input.txt", "r")

def findS(i, j):
    global answer
    while True:
        i += 1
        if i == n:
            break
        if board[i][j] == 1:
            break
        elif board[i][j] == 2 and not visited[i][j]:
            visited[i][j] = True
            answer += 1
            break

for t in range(10):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(100)] for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            # N인 경우
            if board[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                findS(i, j)
            
    print("#{} {}".format(t +1, answer))