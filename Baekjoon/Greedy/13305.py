"""
백준 - https://www.acmicpc.net/problem/13305

< 주유소 >
"""
import sys

input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_oil = min(oil[: n - 1])  # 가장 작은 리터당 가격
result = 0
for i in range(n - 1):
    if oil[i] != min_oil:  # 현재 도시의 리터당 가격이 가장 작지 않다면,
        result += dist[i] * oil[i]  # 다음 도시까지의 이동거리만큼 주유한다.

    else:  # 현재 도시의 리터당 가격이 가장 작다면,
        sum_dist = sum(dist[i:])  # 최종 도시까지의 거리를 구한다.
        result += sum_dist * oil[i]  # 그 거리까지만큼 주유한다.
        break

print(result)

"""
현재 도시의 기름값보다, 다음 도시들의 기름값이 비싸다면,
현재 도시의 기름값보다 적은 도시까지의 이동거리만큼 미리 주유해야 한다.
"""
import sys

input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
oil = list(map(int, input().split()))

present_oil = oil[0]
min_oil = min(oil[: n - 1])  # 가장 작은 리터당 가격
result = 0
for i in range(n - 1):
    if oil[i] != min_oil:
        if oil[i] > present_oil:  # 도시의 기름값이 기존의 기름값보다 크다면
            result += dist[i] * present_oil  # 기존의 기름값의 가격으로 주유하기
        else:  # 기존의 기름값보다 작다면
            result += dist[i] * oil[i]  # 현재 도시의 기름값으로 주유하고
            present_oil = oil[i]  # present_oil 값으로 반영

    else:  # 현재 도시의 리터당 가격이 가장 작다면,
        sum_dist = sum(dist[i:])  # 최종 도시까지의 거리를 구한다.
        result += sum_dist * oil[i]  # 그 거리까지만큼 주유한다.
        break

print(result)
