'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12899?language=python3

< 124 나라의 숫자 >
'''
def solution(n):
    answer = ''
    while n != 0:
        x = n % 3
        n //= 3
        
        if x == 0:
            n -= 1
            x = 4
        answer += str(x)
            
    return answer[::-1]