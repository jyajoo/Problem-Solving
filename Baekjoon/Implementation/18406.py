'''
백준 - https://www.acmicpc.net/problem/18406

< 럭키 스트레이트 >
'''
import sys

input = sys.stdin.readline

num = input()

num1 = num[:len(num)//2]
num2 = num[len(num)//2:]

sum1 = 0
sum2 = 0
for i in range(len(num)//2):
    sum1 += int(num1[i])
    sum2 += int(num2[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")