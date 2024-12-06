'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/161989

< 덧칠하기 >
'''
def solution(n, m, section):
    answer = 0
    section.sort()
    visited = [False] * n 
    for i in section:
        i -= 1
        if not visited[i]:
            for j in range(i, i + m):
                j %= n
                visited[j] = True
            answer += 1
    return answer
'''
'''
def solution(n, m, section):
    answer = 1
    prev = section[0]
    for i in section:
        if i - prev >= m:
            prev = i
            answer += 1
    return answer