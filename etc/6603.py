'''
백준 - https://www.acmicpc.net/problem/6603

< 로또 >
'''
import sys
from itertools import combinations

input = sys.stdin.readline

arr = [1, 2, 3, 4, 5, 6]

while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1 and arr[0] == 0:
        break

    for i in list(combinations(arr[1:], 6)):
        print(' '.join(map(str, i)))
    
    print()