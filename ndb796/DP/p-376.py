'''
< 금광 >
'''

import sys

input = sys.stdin.readline


def dfs(x, y, result):
    global answer
    if x == n or y == m:
        answer = max(answer, result)
        return

    for dx, dy in direction:
        dfs(x + dx, y + dy, result + board[x][y])


t = int(input())
direction = [(-1, 1), (0, 1), (1, 1)]
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    board = [[0] * m for _ in range(n)]

    a = 0
    for i in range(n):
        for j in range(m):
            board[i][j] = arr[a]
            a += 1

    answer = 0
    for i in range(n):
        dfs(i, 0, 0)
    print(answer)

'''
답안
'''
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index : index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

result = 0
for i in range(n):
    result = max(result, dp[i][m - 1])
print(result)