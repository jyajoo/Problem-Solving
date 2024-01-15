"""
백준 - https://www.acmicpc.net/problem/11478

< 서로 다른 부분 문자열의 개수 >
"""
import sys

input = sys.stdin.readline

s = input()
result = 0

for step in range(1, len(s)):
    arr = []
    for start in range(len(s)):
        if start + step >= len(s):
            break
        arr.append(s[start : start + step])
    arr = list(set(arr))
    result += len(arr)

print(result)