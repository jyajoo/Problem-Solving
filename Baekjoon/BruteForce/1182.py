'''
백준 - https://www.acmicpc.net/problem/1182

< 부분수열의 합 >
'''
import sys

input = sys.stdin.readline

def dfs(step, x):
    global answer
    if step == n:
        if len(x) > 0 and sum(x) == s:
            answer += 1
        return
    dfs(step + 1, x + [arr[step]])
    dfs(step + 1, x)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
dfs(0, [])
print(answer)
