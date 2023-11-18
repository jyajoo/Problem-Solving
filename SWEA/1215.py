"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1&&&&&&&&&&

< [S/W 문제해결 기본] 3일차 - 회문1 >
"""
import sys

sys.stdin = open("C:\Coding\GitHub\Algorithm\SWEA\input (2).txt", "r")


def check(word):
    global answer
    word1, word2 = "", ""
    if len(word) % 2 == 0:
        word1 = word[:len(word)//2]
        word2 = word[len(word)//2:]
    else:
        word1 = word[:len(word)//2]
        word2 = word[len(word)//2 + 1:]
    word2 = word2[::-1]
    if word1 == word2:
        answer += 1


for t in range(10):
    n = int(input())
    board = [list(input()) for _ in range(8)]
    answer = 0
    y = 0

    for x in range(8):
        while True:
            start = y
            end = y + n
            if end > 8:
                break
            word = ""
            word2 = ""
            for j in range(start, end):
                word += board[x][j]
                word2 += board[j][x]
            check(word)
            check(word2)
            y += 1
        y = 0
    print("#{} {}".format(t + 1, answer))

