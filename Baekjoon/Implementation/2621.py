"""
백준 - https://www.acmicpc.net/problem/2621https://www.acmicpc.net/problem/2621

< 카드 게임 >
"""

import sys
from collections import Counter

input = sys.stdin.readline

colors = []
numbers = []
for _ in range(5):
    a, b = input().split()
    b = int(b)
    colors.append(a)
    numbers.append(b)

numbers.sort()


def isContinueNumbers():
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] != 1:
            return False
    return True


score = 0
counter = list(dict(Counter(numbers)).items())
counter.sort(key=lambda x: (-x[1], -x[0]))
max_count = counter[0][1]
max_num = counter[0][0]


if isContinueNumbers() and len(set(colors)) == 1:
    score = numbers[-1] + 900  # 1번 규칙
elif len(set(numbers)) == 2 and max_count == 4:
    score = max_num + 800  # 2번 규칙
elif len(set(numbers)) == 2 and max_count == 3:
    score = max_num * 10 + counter[1][0] + 700  # 3번 규칙
elif len(set(colors)) == 1:
    score = numbers[-1] + 600  # 4번 규칙
elif isContinueNumbers() and len(set(colors)) != 1:
    score = numbers[-1] + 500  # 5번 규칙
elif max_count == 3:
    score = max_num + 400  # 6번 규칙
elif len(set(numbers)) == 3 and max_count == 2:
    score = max_num * 10 + counter[-2][0] + 300  # 7번 규칙
elif max_count == 2:
    score = max_num + 200  # 8번 규칙
else:
    score = max(numbers) + 100
print(score)

"""
"""
import sys

input = sys.stdin.readline

colors = []
numbers = []
for _ in range(5):
    a, b = input().split()
    b = int(b)
    colors.append(a)
    numbers.append(b)

numbers.sort()


def isContinueNumbers():
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] != 1:
            return False
    return True


def sameNumber():
    result, num, arr = 0, 0, []
    for i in list(set(numbers)):
        x = numbers.count(i)
        if result < x:
            result = x
            num = i
        if x > 1:
            arr.append(i)
    return result, num, arr


score = 0
# 모두 같은 색일 때
if len(set(colors)) == 1:
    # 숫자가 연속적일 때
    if isContinueNumbers():
        score = numbers[-1] + 900  # 1번 규칙

    else:
        score = numbers[-1] + 600  # 4번 규칙

# 숫자가 연속적일 때
elif isContinueNumbers():
    score = numbers[-1] + 500  # 5번 규칙

else:
    count, num, arr = sameNumber()

    if count == 3:
        score = num + 400

    elif count == 2:
        score = num + 200

    if len(set(numbers)) == 2:
        # 숫자가 4개가 같을 때
        if count == 4:
            score = num + 800

        # 숫자가 3개가 같고, 나머지 2개도 같을 때
        if count == 3:
            next = 0
            for i in list(set(numbers)):
                if i != num:
                    next = i
            score = num * 10 + next + 700

    elif len(set(numbers)) == 3:
        if count == 2:
            score = max(arr) * 10 + min(arr) + 300

if score == 0:
    score = max(numbers) + 100

print(score)
