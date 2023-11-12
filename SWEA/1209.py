"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

< [S/W 문제해결 기본] 2일차 - Sum >
"""
import sys

sys.stdin = open("C:\coding\github\Algorithm\SWEA\input.txt", "r")

for i in range(10):
    n = int(input())
    answer = 0

    numbers = []
    for _ in range(100):
        numbers.append(list(map(int, input().split())))

    # 행 계산
    for number in numbers:
        answer = max(answer, sum(number))

    # 열 계산
    for idx in range(100):
        sum_number = 0
        for number in numbers:
            sum_number += number[idx]
        answer = max(answer, sum_number)

    # 대각선 계산
    idx = 0
    sum_number = 0
    idx2 = 99
    sum_number2 = 0
    for number in numbers:
        sum_number += number[idx]
        idx += 1
        sum_number2 += number[idx2]
        idx -= 1
    answer = max(answer, sum_number, sum_number2)

    print("#{} {}".format(i + 1, answer))
