"""
백준 - https://www.acmicpc.net/problem/18310

< 안테나 >
"""
import sys
input = sys.stdin.readline

n = int(input())
homes = list(map(int, input().split()))
homes.sort(key = lambda x : x)
print(homes[(len(homes) - 1) // 2])
