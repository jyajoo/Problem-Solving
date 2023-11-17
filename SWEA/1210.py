'''
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1&&&&&&&&&&

< [S/W 문제해결 기본] 2일차 - Ladder1 >
'''
import sys

sys.stdin = open("C:\Coding\GitHub\Algorithm\SWEA\input (1).txt", "r")

def dfs(x, y):
    stack = [(x, y)]

    while True:
        x, y = stack.pop()

        if x == 99:
            return ladder[x][y]            

        trans = False
        for t in transform:
            while 0 <= y + t < 100 and ladder[x][y + t]:
                y += t
                trans = True
            if trans:
                break
        
        stack.append((x + 1, y))

transform = [-1, 1]
for _ in range(10):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    answer = 0
    for i in range(100):
        if ladder[0][i] == 1:
            result = dfs(0, i)
            if result == 2:
                answer = i
                break
    
    print("#{} {}".format(n, answer))