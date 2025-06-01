'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12924?language=python3

< 숫자의 표현 >
'''
def solution(n):
    answer = 0
    
    for start in range(1, n + 1):
        sum_val = start
        while sum_val < n:
            start += 1
            sum_val += start
        if sum_val == n:
            answer += 1
    
    return answer