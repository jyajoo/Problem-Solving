'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/172928

< 공원 산책 >
'''
def solution(park, routes):
    
    direction = {'W' : (0, -1), 'E' : (0, 1), 'S' : (1, 0), 'N' : (-1, 0)}
    
    # 시작 지점 위치 찾기
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j
                break
    
    # 루트에 따라 이동시키기
    for route in routes:
        op, n = route.split()
        fx, fy = x, y
        for i in range(int(n)):
            dx, dy = direction.get(op)
            nx = x + dx
            ny = y + dy
            
            # 만약 벗어나거나, 장애물이 발견되면, 초반 위치로 초기화
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]) or park[nx][ny] == 'X':
                    x, y = fx, fy
                    break
            x, y = nx, ny
    return [x, y]