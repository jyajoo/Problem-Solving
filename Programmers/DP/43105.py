'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/43105

< 정수 삼각형 >
'''
def solution(triangle):
    
    depth = len(triangle)
    dp = [[0] * (i + 1) for i in range(depth)]
    
    for i in range(depth):
        for j in range(i + 1):
            max_val = 0
            if j == 0:
                max_val = max(max_val, dp[i - 1][j])
            elif j == i:
                max_val = max(max_val, dp[i - 1][j - 1])
            else:
                max_val = max(max_val, dp[i - 1][j - 1], dp[i - 1][j])
            dp[i][j] = max_val + triangle[i][j]
    return max(dp[-1])
        
'''
'''
def solution(triangle):
    
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == i:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    return max(triangle[-1])