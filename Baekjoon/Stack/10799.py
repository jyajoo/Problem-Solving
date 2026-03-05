'''
백준 - https://www.acmicpc.net/problem/10799

< 쇠막대기 >
'''
import sys

input = sys.stdin.readline

n = input().strip()

answer = 0

count = 0
for i in range(1, len(n)):
    if n[i - 1] == '(' and n[i] == '(':
        count += 1
    
    elif n[i - 1] == '(' and n[i] == ')':
        answer += count
    
    elif n[i] == ')':
        answer += 1
        count -= 1
print(answer)
'''
'''
import sys

input = sys.stdin.readline

n = input().strip()
stack = []

answer = 0
for i in range(len(n)):
    if n[i] == '(':
        stack.append(n[i])
    elif n[i] == ')':
        stack.pop()
        if n[i - 1] == '(':
            answer += len(stack)
        else:
            answer += 1

print(answer)