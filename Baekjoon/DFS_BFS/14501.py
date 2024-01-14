"""
백준 - https://www.acmicpc.net/problem/14501

< 퇴사 >
"""
import sys
input = sys.stdin.readline

def dfs(x, money):
    global answer
    if x == n + 1:
        answer = max(answer, money)
        return

    # 해당 날짜에 상담을 잡는 경우
    d, m = arr[x - 1]
    if x + d <= n + 1:
        dfs(x + d, money + m)
    
    # 해당 날짜에 상담을 잡지 않는 경우
    dfs(x + 1, money) 

n = int(input())
arr = []
for _ in range(n):
    day, money = map(int, input().split())
    arr.append((day, money))

answer = 0
dfs(1, 0)
print(answer)