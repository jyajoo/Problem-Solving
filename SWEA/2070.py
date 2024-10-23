"""
swea - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

< 큰 놈, 작은 놈, 같은 놈 >
"""
T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    answer = ""
    if a < b:
        answer = "<"
    elif a > b:
        answer = ">"
    elif a == b:
        answer = "="

    print("#%d %c" % (t + 1, answer))