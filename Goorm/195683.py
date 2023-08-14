'''
구름톤챌린지 - https://level.goorm.io/exam/195683/%EC%9A%B4%EB%8F%99-%EC%A4%91%EB%8F%85-%ED%94%8C%EB%A0%88%EC%9D%B4%EC%96%B4/quiz/1

< 운동 중독 플레이어 >
'''
import sys
import math

input = sys.stdin.readline
w, r = map(int, input().split())
print(math.trunc(w * (1 + r/30)))