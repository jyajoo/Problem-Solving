'''
백준 - https://www.acmicpc.net/problem/1003

< 피보나치 함수 >
'''
import sys

input = sys.stdin.readline

t = int(input())
z_arr = [0] * 41
f_arr = [0] * 41

z_arr[0] = 1
f_arr[1] = 1

for i in range(2, 41):
    z_arr[i] = z_arr[i - 1] + z_arr[i - 2]
    f_arr[i] = f_arr[i - 1] + f_arr[i - 2]

for _ in range(t):
    n = int(input())
    print(z_arr[n], f_arr[n])
