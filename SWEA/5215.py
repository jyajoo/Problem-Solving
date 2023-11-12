"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1#

< 햄버거 다이어트 >
"""
from itertools import combinations

T = int(input())

for x in range(T):
    N, L = map(int, input().split())

    lst = []
    for _ in range(N):
        T, K = map(int, input().split())
        lst.append((T, K))

    answer = 0
    for i in range(N, -1, -1):
        for c in combinations(lst, i):
            score = 0
            calorie = 0
            for m, n in c:
                score += m
                calorie += n
            if calorie > L:
                continue
            answer = max(answer, score)


    print("#{} {}".format(x + 1, answer))
