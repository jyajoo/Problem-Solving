"""
백준 - https://www.acmicpc.net/problem/18870

< 좌표 압축 >
"""
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

sort_numbers = sorted(set(numbers))
index_numbers = [i for i in range(len(sort_numbers))]
dict_numbers = dict(zip(sort_numbers, index_numbers))

for i in numbers:
    print(dict_numbers.get(i), end = " ")