'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/161990

< 바탕화면 정리 >
'''
def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                a.append(i)
                b.append(j)
    
    return [min(a), min(b), max(a) + 1, max(b) + 1]