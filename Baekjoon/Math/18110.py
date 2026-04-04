'''
백준 - https://www.acmicpc.net/problem/18110

< solved.ac >
'''
import sys

input = sys.stdin.readline

def my_round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    return int(n)

n = int(input())

arr = [int(input()) for _ in range(n)]

if len(arr) == 0:
    print(0)
else:
    count = my_round(len(arr) * 0.15)
    arr.sort()
    start = count
    end = len(arr) - count
    target = arr[start : end]
    print(my_round(sum(target) / len(target)))
