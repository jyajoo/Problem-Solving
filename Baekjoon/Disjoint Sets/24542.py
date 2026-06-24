'''
백준 - https://www.acmicpc.net/problem/24542

< 튜터 - 튜티 관계의 수 >
'''
import sys

input = sys.stdin.readline

def find_parent(x):
    if union[x] < 0:
        return x
    else:
        union[x] = find_parent(union[x])
        return union[x]

def find_union(x, y):
    a = find_parent(x)
    b = find_parent(y)

    if a == b:
        return False
    else:
        union[a] += union[b]
        union[b] = a
        return True

n, m = map(int, input().split())
union = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    find_union(a, b)

answer = 1
for i in range(1, n + 1):
    if union[i] < 0:
        answer *= -union[i] % 1000000007
print(answer % 1000000007)