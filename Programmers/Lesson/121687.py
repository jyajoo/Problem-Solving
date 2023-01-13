'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/15009/lessons/121687

< 실습용 로봇 >
'''
def solution(command):
    direction = ['w', 'd', 's', 'a']
    G = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    answer = []
    x = 0
    y = 0
    idx = 0
    for i in command:
        if i == "R":
            idx += 1
            if idx == 4:
                idx = 0
        elif i == "L":
            idx -= 1
            if idx == -1:
                idx = 3
        elif i == "G":
            x += G[idx][0]
            y += G[idx][1]
        elif i == "B":
            x -= G[idx][0]
            y -= G[idx][1]
                
    answer = [x, y]
    return answer