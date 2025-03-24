"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42584

< 주식 가격 >
"""


def solution(prices):
    answer = [0] * len(prices)
    prev = []
    for idx, price in enumerate(prices):
        while prev and price < prev[-1][1]:
            pi, pp = prev.pop()
            answer[pi] = idx - pi
        prev.append((idx, price))

    while prev:
        pi, pp = prev.pop()
        answer[pi] = len(prices) - 1 - pi
    return answer


"""
참고 - https://school.programmers.co.kr/questions/20326?question=20326
"""


def solution(prices):
    answer = [0] * len(prices)

    stack = []
    for i in range(len(prices)):
        price = prices[i]
        while stack and prices[stack[-1]] > price:
            x = stack.pop()
            answer[x] = i - x
        stack.append(i)

    while stack:
        x = stack.pop()
        answer[x] = len(prices) - 1 - x

    return answer

'''
'''
from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    q = deque()
    
    for idx, i in enumerate(prices):
        for _ in range(len(q)):
            x, n, cnt = q.popleft()
            if n <= i:
                cnt += 1
                q.append((x, n, cnt))
                answer[x] = cnt
            else:
                answer[x] = cnt + 1
        q.append((idx, i, 0))
    return answer