'''
백준 - https://www.acmicpc.net/problem/4949

< 균형잡힌 세상 >
'''
import sys

input = sys.stdin.readline

while True:
    n = input().rstrip()
    if len(n) == 1 and n[0] == '.':
        break

    stack = []
    flag = False
    for i in n:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if len(stack) == 0:
                flag = True
                break
            x = stack[-1]
            if (i == ')' and x == '(') or (i == ']' and x == '['):
                stack.pop()
                continue
            else:
                flag = True
                break
    if stack or flag:
        print('no')
    else:
        print('yes')