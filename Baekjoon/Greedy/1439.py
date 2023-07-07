"""
백준 - https://www.acmicpc.net/problem/1439
< 뒤집기 >
"""
import sys

input = sys.stdin.readline

s = input()

pre_num = s[0]
zero = 0
one = 0

for i in range(1, len(s)):
    if pre_num != s[i]:
        if pre_num == "0":
            zero += 1
        else:
            one += 1
        pre_num = s[i]
print(min(zero, one))

"""
"""
s = input()

zero = 0
one = 0

if s[0] == "0":
    zero += 1
else:
    one += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == "0":
            zero += 1
        else:
            one += 1

print(min(zero, one))
