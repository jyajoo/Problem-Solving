"""
백준 - https://www.acmicpc.net/problem/30889

< 좌석 배치도 >
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input().rstrip())

movie = [['.' for _ in range(20)] for _ in range(10)]

for chair in arr:
    x = ord(chair[0]) - 65
    y = int(chair[1:]) - 1

    movie[x][y] = 'o'

for i in movie:
    print(''.join(i))
