"""
백준 - https://www.acmicpc.net/problem/1427

< 소트인사이드 >
"""
import sys

input = sys.stdin.readline

n = list(input().strip())
n.sort(key= lambda x : -int(x))
print(''.join(n))