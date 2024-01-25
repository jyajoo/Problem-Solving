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
"""
"""
import sys
input = sys.stdin.readline

def move(lst):
    global result
    while lst:
        result += abs(lst.pop()) * 2
        for _ in range(m - 1):
            if not lst:
                return
            lst.pop()

n, m = map(int, input().split())
pos = [0]
neg = [0]
for n in map(int, input().split()):
    if n > 0:
        pos.append(n)
    else:
        neg.append(n)

pos.sort(key=lambda x: x)
neg.sort(key=lambda x: -x)

result = 0
result -= max(pos[-1], -neg[-1])
move(pos)
move(neg)
print(result)