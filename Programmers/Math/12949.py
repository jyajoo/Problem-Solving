'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12949

< 행렬의 곱셈 >
'''
def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            for a in range(len(arr2)):
                answer[i][j] += arr1[i][a] * arr2[a][j]
    
    return answer