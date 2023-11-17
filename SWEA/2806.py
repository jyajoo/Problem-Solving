"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

< N-Queen >
"""


def dfs(x):
    global answer
    if x == n:
        answer += 1
        return
    
    for j in range(n):
        if row[j] == diagonal[x - j] == diagonal2[x + j] == 0:
            row[j] = diagonal[x - j] = diagonal2[x + j] = 1
            dfs(x + 1)
            row[j] = diagonal[x - j] = diagonal2[x + j] = 0
            


T = int(input())
for t in range(T):
    n = int(input())
    row = [0] * n
    diagonal, diagonal2 = [[0] * (2 * n) for _ in range(2)]
    answer = 0
    dfs(0)
    print("#{} {}".format(t + 1, answer))
