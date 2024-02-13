"""
백준 - https://www.acmicpc.net/problem/1132

< 합 >
"""
import sys
input = sys.stdin.readline

n = int(input())
nums = [input().strip() for _ in range(n)]

alpha = {}
not_zero = []
for num in nums:
    if num[0] not in not_zero:
        not_zero.append(num[0])
    
    # 가장 큰 수가 되기 위해 자릿수가 높은만큼 점수 매기기
    for i in range(len(num)):
        score = 10 ** (len(num) - i)
        if num[i] not in alpha:
            alpha[num[i]] = 0
        alpha[num[i]] += score


sort_alpha = sorted(alpha, key= lambda x : -alpha[x])
numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0]
numbers = numbers[: len(sort_alpha)]

# 0이 되면 안되는 경우(A), 
# 0이 되어도 상관없으며 점수가 가장 낮은 수(B)의 점수를 A 점수보다 낮춘다.
for i in range(len(sort_alpha) - 1, -1, -1):
    a = sort_alpha[i]
    if numbers[i] == 0 and a in not_zero:
        for j in range(len(sort_alpha) - 1, -1, -1):
            b = sort_alpha[j]
            if numbers[j] != 0 and b not in not_zero:
                alpha[b] = alpha[a] - 1
                break

sort_alpha = sorted(alpha, key=lambda x: -alpha[x])

answer = 0
for num in nums:
    m = ""
    for i in num:
        idx = sort_alpha.index(i)
        m += str(numbers[idx])
    answer += int(m)

print(answer)
