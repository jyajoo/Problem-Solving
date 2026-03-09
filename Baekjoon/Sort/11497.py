'''
백준 - https://www.acmicpc.net/problem/11497

< 통나무 건너뛰기 >
'''
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort(reverse=True)
    new = deque()
    new.append(trees[0])
    for i in range(1, n, 2):
        if i == n - 1:
            new.appendleft(trees[i])
        else:
            a, b = trees[i], trees[i + 1]
            new.appendleft(b)
            new.append(a)

    answer = 0
    for i in range(n):
        if i == n - 1:
            a, b = new[i], new[0]
        else:
            a, b = new[i], new[i + 1]
        answer = max(answer, abs(a - b))
    print(answer)