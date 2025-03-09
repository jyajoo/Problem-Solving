'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/389478

< 택배 상자 꺼내기 >
'''
def solution(n, w, num):
    boxes = [[0] * w for _ in range(n // w + 1)]
    x, y = 0, 0
    target_x, target_y = 0, 0
    for i in range(1, n + 1):
        boxes[x][y] = i
        if i == num:
            target_x, target_y = x, y
        if x % 2 == 0:
            y += 1
            if y == w:
                y -= 1
                x += 1
        else:
            y -= 1
            if y < 0:
                y += 1
                x += 1
    
    answer = (n // w + 1) - target_x
    if boxes[n // w][target_y] == 0:
        answer -= 1
    
    return answer