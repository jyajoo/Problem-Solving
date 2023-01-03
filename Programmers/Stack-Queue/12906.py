'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12906

< 같은 숫자는 싫어 >
'''

def solution(arr):
    answer = []
    for i in arr:
        if len(answer) != 0:
            p = answer.pop()
            if p != i:
                answer.append(p)
                answer.append(i)
            else:
                answer.append(p)
        else:
            answer.append(i)    
    return answer

'''
'''
def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)
    return answer