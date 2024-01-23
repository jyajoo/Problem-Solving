"""
백준 - https://www.acmicpc.net/problem/1461

< 도서관 >
"""
import sys

input = sys.stdin.readline
from collections import deque

# 책 개수, 한 번에 들 수 있는 책의 개수
n, m = map(int, input().split())
books = list(map(int, input().split()))
books.sort(key=lambda x: x)
pos = deque()
neg = deque()

for i in books:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)

result = 0
if len(neg) > 0 and len(pos) > 0:
    if abs(neg[0]) > abs(pos[-1]):
        result = abs(neg[0])
        for i in range(m):
            if len(neg) > 0:
                neg.popleft()
    else:
        result = abs(pos[-1])
        for i in range(m):
            if len(pos) > 0:
                pos.pop()
elif len(neg) > 0:
    result = abs(neg[0])
    for i in range(m):
        if len(neg) > 0:
            neg.popleft()
else:
    result = abs(pos[-1])
    for i in range(m):
        if len(pos) > 0:
            pos.pop()
while neg:
    result += abs(neg.popleft()) * 2
    for i in range(m - 1):
        if len(neg) > 0:
            neg.popleft()

while pos:
    result += pos.pop() * 2
    for i in range(m - 1):
        if len(pos) > 0:
            pos.pop()

print(result)
