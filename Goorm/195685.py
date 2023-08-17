"""
구름톤 챌린지 - https://level.goorm.io/exam/195685/%ED%95%A9-%EA%B3%84%EC%82%B0%EA%B8%B0/quiz/1

< 합 계산기 >
"""
import sys

input = sys.stdin.readline

T = int(input())
result = 0
for _ in range(T):
    num1, s, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    if s == "+":
        result += num1 + num2
    elif s == "-":
        result += num1 - num2
    elif s == "*":
        result += num1 * num2
    elif s == "/":
        result += num1 // num2

print(result)
