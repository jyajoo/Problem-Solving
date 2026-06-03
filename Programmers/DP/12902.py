'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12902

< 3 x n 타일링 >
'''
def solution(n):
    dp = [0] * (n + 1)
    if n < 2:
        return 0
    dp[2] = 3
    val = 0
    for i in range(3, n + 1):
        if i % 2 == 0:
            dp[i] = (dp[i - 2] * 3 + val + 2) % 1000000007
            val += dp[i - 2] * 2
    return dp[n]