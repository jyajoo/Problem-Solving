"""
백준 - https://www.acmicpc.net/problem/2141

< 우체국 >
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = []
total_peoeple = 0
for _ in range(n):
    village, people = map(int, input().split())
    arr.append((village, people))
    total_peoeple += people

# 마을의 위치가 섞여서 입력될 수 있으므로, 마을의 위치를 기준으로 정렬
arr.sort(key=lambda x: x[0])

dist = 0
for village, people in arr:
    dist += people

    # 총 인원의 절반값보다 크거나 같아지는 순간이 우체국 위치로 가장 적절하다.
    if dist >= total_peoeple / 2:
        print(village)
        break