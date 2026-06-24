'''
백준 - https://www.acmicpc.net/problem/2230

< 수 고르기 >
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

start = 0
end = 0
answer = int(2e9)
while start <= end and end < n:
    diff = numbers[end] - numbers[start]

    if diff >= m:
        answer = min(answer, diff)
        start += 1
    else:
        end += 1

print(answer)
