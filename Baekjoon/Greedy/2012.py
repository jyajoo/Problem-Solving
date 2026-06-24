'''
백준 - https://www.acmicpc.net/problem/2012

< 등수 매기기 >
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
answer = 0
for i in range(n):
    answer += abs((i + 1) - arr[i])
print(answer)