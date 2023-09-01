"""
구름톤 챌린지 - https://level.goorm.io/exam/195697/%EA%B3%BC%EC%9D%BC-%EA%B5%AC%EB%A7%A4/quiz/1

< 과일 구매 >
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # 과일 종류(n), 가진 돈(k)

fruit = []
for i in range(n):
    p, c = map(int, input().split())  # 가격(p), 포만감(c)
    fruit.append((p, c))

fruit.sort(key=lambda x: (-x[1] / x[0], -x[0]))
result = 0
for p, c in fruit:
    if p <= k:
        k -= p
        result += c
        continue
    else:
        # p만큼 돈 차감 후 포만감 c만큼 충당 가능
        for i in range(k):
            if k >= 1:
                k -= 1
                result += c // p


print(result)
