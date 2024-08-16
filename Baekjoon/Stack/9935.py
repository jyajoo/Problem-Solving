"""
백준 - https://www.acmicpc.net/problem/9935

< 문자열 폭발 >
"""

from sys import stdin

input = stdin.readline

string = input().strip()
bomb = input().strip()
new_string = []
for i in string:
    new_string.append(i)
    if len(new_string) >= len(bomb):
        if "".join(new_string[-len(bomb) :]) == bomb:
            for _ in range(len(bomb)):
                new_string.pop()

# # 남아있는 문자가 없다면, "FRULA" 출력
if len(new_string) == 0:
    print("FRULA")
else:
    print("".join(new_string))

"""
"""
from sys import stdin

input = stdin.readline

string = input().strip()
bomb = input().strip()
new_string = []
for i in string:
    new_string.append(i)
    if i == bomb[-1] and "".join(new_string[-len(bomb) :]) == bomb:
        del new_string[-len(bomb) :]

# # 남아있는 문자가 없다면, "FRULA" 출력
if len(new_string) == 0:
    print("FRULA")
else:
    print("".join(new_string))
