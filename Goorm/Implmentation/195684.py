"""
구름톤 챌린지 - https://level.goorm.io/exam/195684/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%A7%A4%EB%8B%88%EC%A7%95/quiz/1

< 프로젝트 매니징 >
"""
import sys

input = sys.stdin.readline

n = int(input())
t, m = map(int, input().split())
for _ in range(n):
    m += int(input())
    t += m // 60
    m %= 60
    if t > 23:
        t %= 24

print(t, m)

"""
"""
import sys

input = sys.stdin.readline

n = int(input())
t, m = map(int, input().split())
time = 0
for _ in range(n):
    time += int(input())

t = (t + time // 60) % 24
m = m + time % 60
if m > 59:
    t += m // 60
    m %= 60
    t %= 24

print(t, m)

"""
"""
import sys

input = sys.stdin.readline

N = int(input())
T, M = map(int, input().split())
c = [int(input()) for _ in range(N)]

time = (T * 60 + M + sum(c)) % 1440
hour = time // 60
minute = time % 60

print(hour, minute)
