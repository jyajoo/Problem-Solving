"""
백준 - https://www.acmicpc.net/problem/30892

< 상어 키우기 >
"""
import sys
import heapq
from collections import deque
input = sys.stdin.readline

# 상어 수, 먹을 수 있는 최대 상어 수, 샼의 크기
n, k, t = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort(key=lambda x: x)
dq = deque(lst)
idx = 0
q = []

while dq and dq[0] < t:
    x = dq.popleft()
    heapq.heappush(q, (-x, x))

count = 0
while count < k and q:
    _, s = heapq.heappop(q)
    if s < t:
        count += 1
        t += s
    else:
        break

    while dq and dq[0] < t:
        x = dq.popleft()
        heapq.heappush(q, (-x, x))

print(t)
"""
- 시간 초과
"""
import sys

input = sys.stdin.readline

# 상어 수, 먹을 수 있는 최대 상어 수, 샼의 크기
n, k, t = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort(key=lambda x: -x)
count = 0
while count < k:
    flag = False
    for s in lst:
        if t > s:
            t += s
            lst.remove(s)
            flag = True
            break

    if flag:
        count += 1
    else:
        break

print(t)
