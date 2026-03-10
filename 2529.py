'''
백준 - https://www.acmicpc.net/problem/2529

< 부등호 >
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = input().split()

def func(step, val):
    global answer
    if step == -1:
        for i in range(0, 10):
            func(step + 1, val + str(i))

    elif step != n:
        v = int(val[-1])
        x = arr[step]
        if x =='<':
            for i in range(v + 1, 10):
                if str(i) not in val:
                    func(step + 1, val + str(i))
        else:
            for i in range(0, v):
                if str(i) not in val:
                    func(step + 1, val + str(i))
    
    else:
        answer.append(val)


answer = []
func(-1, '')
print(answer[-1])
print(answer[0])