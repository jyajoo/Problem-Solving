"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12907

< 거스름돈 >
"""


def solution(n, money):

    dp = [0] * (n + 1)
    dp[0] = 1

    for m in money:
        for i in range(1, n + 1):
            if i - m >= 0:
                dp[i] += dp[i - m]

    return dp[-1]
