"""
백준 - https://www.acmicpc.net/problem/10825

< 국영수 >
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    name, s1, s2, s3 = input().split()
    arr.append((name, int(s1), int(s2), int(s3)))

arr.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for name, _, _, _ in arr:
    print(name)
