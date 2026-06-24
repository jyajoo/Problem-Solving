'''
백준 - https://www.acmicpc.net/problem/2805

< 나무 자르기 >
'''
import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees = dict(Counter(trees))
start = 0
end = max(trees)
answer = 0
while start <= end:
    middle = (start + end) // 2
    result = 0
    for i, j in trees.items():
        if i >= middle:
            result += (i - middle) * j
    
    if result >= m:
        answer = max(answer, middle)
        start = middle + 1
    else:
        end = middle - 1


print(answer)