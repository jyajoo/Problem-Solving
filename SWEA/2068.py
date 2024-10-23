"""
swea - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

< 최대수 구하기 >
"""
T = int(input())
for t in range(T):
    arr = list(map(int, input().split()))
    answer = max(arr)

    print("#%d %d" % (t + 1, answer))
