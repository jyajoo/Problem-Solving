'''
백준 - https://www.acmicpc.net/problem/4948

< 베르트랑 공준ㅇ >
'''
import sys

input = sys.stdin.readline

x = 123456 * 2 + 1
arr = [True for _ in range(x)]

for i in range(2, int(x ** 1/2) + 1):
    if arr[i]:
        j = 2
        while i * j <= x:
            arr[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break
    answer = 0
    for i in range(n + 1, 2 * n + 1):
        if arr[i]:
            answer += 1
    print(answer)