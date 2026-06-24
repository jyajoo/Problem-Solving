'''
백준 - https://www.acmicpc.net/problem/9093

< 단어 뒤집기 >
'''
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = input().split()
    print(n)
    for i in n:
        print(i[::-1], end = " ")
    print()