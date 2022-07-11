'''
백준 - https://www.acmicpc.net/problem/16173

<점프왕 쩰리>
0 1 2
3 4 5
6 7 8
'''

def dfs(x, y, arr, visited):
    global check
    # 방문했는지 확인하기
    if visited[x][y]:
        return

    visited[x][y] = True

    # 승리지점인지 확인하기
    if arr[x][y] == -1:
        check = 1
        return

    # 범위를 벗어나는지 확인하기
    if arr[x][y] + y < len(arr):
        dfs(x, arr[x][y] + y, arr, visited)
    if arr[x][y] + x < len(arr):
        dfs(arr[x][y] + x, y, arr, visited)


global check
check = 0
n = int(input())
arr = []
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().split())))

dfs(0, 0, arr, visited)

if check == 1:
    print("HaruHaru")
else:
    print("Hing")