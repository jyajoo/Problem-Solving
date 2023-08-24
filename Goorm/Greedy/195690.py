"""
구름톤 챌린지 - https://level.goorm.io/exam/195690/%ED%86%B5%EC%A6%9D/quiz/1

< 통증 >
"""
import sys

input = sys.stdin.readline

n = int(input())
count = 0

count += n // 14
n %= 14

count += n // 7
n %= 7

count += n
print(count)
