"""
백준 - https://www.acmicpc.net/problem/6603

< 로또 >
"""
import sys

input = sys.stdin.readline


def combi(arr, data):
    if len(data) == 6:
        print(*data)
        return

    for i in range(len(arr)):
        new_data = data + [arr[i]]
        new_arr = arr[i + 1 :]
        combi(new_arr, new_data)


while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        break
    k = arr[0]
    s = arr[1:]

    combi(s, [])
    print()
