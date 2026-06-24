'''
백준 - https://www.acmicpc.net/problem/11656

< 접미사 배열 >
'''
import sys

input = sys.stdin.readline

n = input().strip()

arr = []
for i in range(len(n)):
    arr.append(n[i:])

arr.sort()
for i in arr:
    print(i)