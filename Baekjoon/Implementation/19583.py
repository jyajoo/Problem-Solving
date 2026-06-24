'''
백준 - https://www.acmicpc.net/problem/19583

< 싸이버개강총회 >
'''
import sys

input = sys.stdin.readline

s, e, q = input().split()
sh, sm = map(int, s.split(":"))
eh, em = map(int, e.split(":"))
qh, qm = map(int, q.split(":"))
s = sh * 60 + sm
e = eh * 60 + em
q = qh * 60 + qm

start = set()
end = set()

while True:
    try:
        time, nickname = input().split()
        h, m = map(int, time.split(":"))
        time = h * 60 + m
        # 시작
        if time >= 0 and time <= s:
            start.add(nickname)

        # 끝 ~ 스트리밍 끝
        elif time >= e and time <= q:
            end.add(nickname)

    except:
        break

print(len(start & end))