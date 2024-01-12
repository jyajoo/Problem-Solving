"""
백준 - https://www.acmicpc.net/problem/25827

< 시간 구간 다중 업데이트 다중 합 >
"""
"""
백준 - https://www.acmicpc.net/problem/25827

< 시간 구간 다중 업데이트 다중 합 >
"""
import sys

input = sys.stdin.readline
n = int(input())

time = [0] * (24 * 60 * 60)
result = [0] * (24 * 60 * 60)
flag = True
for _ in range(n):
    cmd, start, end = input().split()
    h1, m1, s1 = map(int, start.split(":"))
    h2, m2, s2 = map(int, end.split(":"))
    start_time = s1 + 60 * m1 + 60 * 60 * h1
    end_time = s2 + 60 * m2 + 60 * 60 * h2

    if cmd == "1":
        time[start_time] += 1
        time[end_time] -= 1

    else:
        if flag:
            step = time[0]
            result[0] = step
            for i in range(1, len(time)):
                step += time[i]
                result[i] = result[i - 1] + step
            flag = False

        if start_time == 0:
            print(result[end_time - 1])
        else:
            print(result[end_time - 1] - result[start_time - 1])
