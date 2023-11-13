"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWczm7QaACgDFAWn&categoryId=AWczm7QaACgDFAWn&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

< 삼성시의 버스 노선 >
"""
from collections import defaultdict

T = int(input())

for x in range(T):
    n = int(input())
    numbers = []
    for _ in range(n):
        a, b = map(int, input().split())
        numbers.append((a, b))
    result = defaultdict(int)
    while numbers:
        n, m = numbers.pop()
        for i in range(n, m + 1):
            result[i] += 1

    p = int(input())
    p_num = []
    for i in range(1, p + 1):
        c = int(input())
        p_num.append(c)

    print("#%d" % (x + 1), end = " ")
    for i in range(p):
        print("%d" % (result[p_num[i]]), end=" ")
    print()
