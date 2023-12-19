"""
백준 - https://www.acmicpc.net/problem/9663

< N-Queen >
"""
import sys

input = sys.stdin.readline


def dfs(step):
    global answer
    if step == n:
        answer += 1
        return

    for j in range(n):
        if not v1[j] and not v2[step + j] and not v3[step - j]:
            v1[j] = v2[step + j] = v3[step - j] = True
            dfs(step + 1)
            v1[j] = v2[step + j] = v3[step - j] = False


n = int(input())
v1 = [False] * n
v2 = [False] * (2 * n)
v3 = [False] * (2 * n)
answer = 0
dfs(0)
print(answer)
