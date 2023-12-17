"""
백준 - https://www.acmicpc.net/problem/14888

< 연산자 끼워넣기 >
"""
import sys


def dfs(number, x):
    global min_answer, max_answer
    if x == n:
        min_answer = min(min_answer, number)
        max_answer = max(max_answer, number)
        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            if i == 0:
                dfs(number + num[x], x + 1)
            elif i == 1:
                dfs(number - num[x], x + 1)
            elif i == 2:
                dfs(number * num[x], x + 1)
            else:
                dfs(int(number / num[x]), x + 1)
            op[i] += 1


input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

max_answer = -int(1e9)
min_answer = int(1e9)
dfs(num[0], 1)
print(max_answer)
print(min_answer)
