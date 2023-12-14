"""
백준 - https://www.acmicpc.net/problem/1436

< 영화감독 숌 >
"""
import sys

input = sys.stdin.readline
n = int(input())
count = 0
result = 666
while True:
    if '666' in str(result):
        count += 1
    
    if count == n:
        break

    result += 1

print(result)