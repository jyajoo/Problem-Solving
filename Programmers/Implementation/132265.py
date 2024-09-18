"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/132265

< 롤케이크 자르기 >
"""

from collections import defaultdict
import copy


def solution(topping):
    answer = 0
    type = len(set(topping))

    a = defaultdict(int)
    b = defaultdict(int)

    middle = len(topping) // 2
    for i in range(middle):
        t = topping[i]
        a[t] += 1

    for i in range(middle, len(topping)):
        t = topping[i]
        b[t] += 1

    if len(a) == len(b):
        answer += 1

    # 오른쪽으로 이동
    x = copy.deepcopy(a)
    y = copy.deepcopy(b)
    for i in range(middle, len(topping)):
        t = topping[i]
        x[t] += 1
        y[t] -= 1
        if y[t] == 0:
            del y[t]
        if len(x) == len(y):
            answer += 1

    # 왼쪽으로 이동
    x = copy.deepcopy(a)
    y = copy.deepcopy(b)
    for i in range(middle - 1, -1, -1):
        t = topping[i]
        x[t] -= 1
        y[t] -= 1
        if x[t] == 0:
            del x[t]
        if len(x) == len(y):
            answer += 1

    return answer


"""
"""
from collections import defaultdict


def solution(topping):
    answer = 0
    a = defaultdict(int)
    b = defaultdict(int)

    # 모든 토핑을 b에 넣음
    for t in topping:
        b[t] += 1

    # 왼쪽으로 이동하며 a에 추가하고 b에서 제거
    for t in topping:
        a[t] += 1
        b[t] -= 1
        if b[t] == 0:
            del b[t]

        # 공평하게 나누어지는지 체크
        if len(a) == len(b):
            answer += 1

    return answer
