'''
백준 - https://www.acmicpc.net/problem/4307

< 개미 >
'''
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    i, n = map(int, input().split())
    
    short, long = 0, 0
    for _ in range(n):
        a = int(input())
        short = max(short, min(a, i - a))
        long = max(long, max(a, i - a))

    print(short, long)
