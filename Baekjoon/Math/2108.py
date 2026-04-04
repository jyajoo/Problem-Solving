'''
백준 - https://www.acmicpc.net/problem/2108

< 통계학 >
'''
import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

print(round(sum(arr) / len(arr)))

arr.sort()
print(arr[len(arr) // 2])

counter = defaultdict(int)
for i in arr:
    counter[i] += 1

counter = list(counter.items())
counter.sort(key = lambda x : (-x[1], x[0]))
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print(counter[1][0])
else:
    print(counter[0][0])

print(max(arr) - min(arr))