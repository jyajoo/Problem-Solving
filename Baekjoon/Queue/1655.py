"""
백준 - https://www.acmicpc.net/problem/1655

< 가운데를 말해요 >
"""

from sys import stdin
import heapq

input = stdin.readline

n = int(input())

left = []
right = []
middle = int(input())  # 첫 번째 수를 중간값으로 지정
result = [middle]

for i in range(2, n + 1):
    current = int(input())

    if current < middle:
        heapq.heappush(left, -current)
        # 현재 개수가 짝수인 경우
        if i % 2 == 0:
            # middle을 right로 옮기고
            # left의 가장 큰 값을 middle로 지정
            heapq.heappush(right, middle)
            middle = -heapq.heappop(left)
    else:
        heapq.heappush(right, current)
        # 현재 총 개수가 홀수인 경우
        # middle을 left로 옮기고
        # right의 가장 작은 값을 middle로 지정
        if i % 2 != 0:
            heapq.heappush(left, -middle)
            middle = heapq.heappop(right)

    result.append(middle)

print("\n".join(map(str, result)))
