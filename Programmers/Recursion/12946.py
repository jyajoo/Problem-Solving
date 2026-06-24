'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12946?language=python3

< 하노이의 탑 >
'''
def solution(n):
    answer = []
    
    def hanoi(n, start, to, via):
        if n == 0:
            return
        
        hanoi(n - 1, start, via, to)
        answer.append([start, to])
        hanoi(n - 1, via, to, start)
    
    hanoi(n, 1, 3, 2)
    
    return answer