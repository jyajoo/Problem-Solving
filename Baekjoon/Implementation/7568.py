'''
백준 - https://www.acmicpc.net/problem/7568

< 덩치 >
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

count = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        a, b = arr[i]
        x, y = arr[j]
        if a > x and b > y:
            count[j] += 1
        elif a < x and b < y:
            count[i] += 1

result = [0] * n
rate = 1
for i in range(n):
    for idx, j in enumerate(count):
        if j == i:
            result[idx] = rate
    rate += 1
print(*result)
