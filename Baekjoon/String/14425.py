'''
백준 - https://www.acmicpc.net/problem/14425


'''
n, m = map(int, input().split())
s = set()
cnt = 0

for _ in range(n):
    s.add(input())

for _ in range(m):
    a = input()
    if a in s:
        cnt += 1
print(cnt)