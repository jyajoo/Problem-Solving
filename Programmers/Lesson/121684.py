'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/15008/lessons/121684

< [PCCP 모의고사 1] 2번 >

'''

from itertools import permutations

def solution(ability):
    
    student = [i for i in range(len(ability))]
    answer = 0
    arr = list(permutations(student, len(ability[0])))
    for i in arr:
        num = 0
        for j in range(len(ability[0])):
            num += ability[i[j]][j]
        answer = max(answer, num)
    return answer