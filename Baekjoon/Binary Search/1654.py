'''
백준 - https://www.acmicpc.net/problem/1654

< 랜선 자르기 >
'''
import sys

input = sys.stdin.readline

k, n = map(int, input().split())

arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)
result = 0
while start <= end:
    middle = (start + end) // 2
    count = 0
    for i in arr:
        count += i // middle
    
    if count < n:
        end = middle - 1

    else:
        start = middle + 1
        result = max(result, middle)

print(result)