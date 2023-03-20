''' 
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42747

< H-Index >
'''
def solution(citations):
    answer = 0
    citations.sort(key = lambda x : -x)
    for i in range(len(citations) + 1):
        if i == len(citations):
            answer = i
            break
        if citations[i] <= i:
            answer = i
            break
    return answer