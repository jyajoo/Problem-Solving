'''
백준 - https://www.acmicpc.net/problem/14225

< 부분수열의 합 >
'''
import sys

input = sys.stdin.readline

def dfs(idx, current):
    global numbers
    numbers.add(current)
    
    if idx == n:
        return

    dfs(idx + 1, current + s[idx])
    dfs(idx + 1, current)

n = int(input())
s = list(map(int, input().split()))
s.sort()
numbers = set(s)
dfs(0, 0)

numbers = list(numbers)
numbers.sort()
answer = 0
for i in range(len(numbers)):
    if i != numbers[i]:
        answer = i
        break
if answer == 0:
    answer = numbers[-1] + 1
print(answer)
'''
'''
import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
s.sort()
target = 1
for i in s:
    if i <= target:
        target += i
    else:
        break
print(target)