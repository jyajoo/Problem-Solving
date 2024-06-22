"""
백준 - https://www.acmicpc.net/problem/1932

< 정수 삼각형 >
- 시간 초과
"""
# import sys

# input = sys.stdin.readline


# def dfs(step, val, idx):
#     global answer
#     if step == n:
#         answer = max(answer, val)
#         return
#     dfs(step + 1, val + arr[step][idx], idx)
#     dfs(step + 1, val + arr[step][idx], idx + 1)


# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# answer = 0
# dfs(0, 0, 0)
# print(answer)
'''
- dp
'''
import sys

input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        
        dp[i][j] += max(up_left, up)

print(max(dp[-1]))

'''
2차원 리스트 사용 -> 1차원 리스트 두개로
공간 복잡도를 줄일 수 있다.
'''
import sys

input = sys.stdin.readline

n = int(input())
dp_prev = list(map(int, input().split()))

for i in range(1, n):
    dp_curr = list(map(int, input().split()))
    for j in range(i + 1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp_prev[j - 1]
        
        if j == i:
            up = 0
        else:
            up = dp_prev[j]

        dp_curr[j] += max(up_left, up)
    
    dp_prev = dp_curr

print(max(dp_prev))

'''
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    if i == 0:
        continue

    for j in range(i + 1):
        if j == 0:  # 오른쪽 위만 가능(인덱스 변동 없음)
            arr[i][j] += arr[i - 1][j]
        elif j == i:  # 왼쪽 위만 가능(인덱스 - 1)
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])

print(max(arr[-1]))
