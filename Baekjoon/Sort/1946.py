"""
백준 - https://www.acmicpc.net/problem/1946

< 신입 사원 >
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        x_rank, y_rank = map(int, input().split())
        arr.append((x_rank, y_rank))

    arr.sort(key=lambda x: (x[0], x[1]))

    x, y = arr[0][0], arr[0][1]
    count = 0
    for x_rank, y_rank in arr:
        if x_rank <= x or y_rank <= y:
            count += 1
            x, y = x_rank, y_rank

    print(count)
