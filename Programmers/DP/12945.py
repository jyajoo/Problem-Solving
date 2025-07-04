'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12945

< 피보나치 수 >
'''
def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    
    return dp[-1] % 1234567
    