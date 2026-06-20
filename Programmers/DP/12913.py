'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12913

< 땅 따먹기 >
'''
def solution(land):
    dp = [[0] * len(land[0]) for _ in range(len(land))]
    
    dp[0] = land[0]
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            dp[i][j] = land[i][j] + max(dp[i - 1][:j] + dp[i - 1][j + 1:])
    
    return max(dp[-1])