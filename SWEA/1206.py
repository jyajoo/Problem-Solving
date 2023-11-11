"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh

< [S/W 문제해결 기본] 1일차 - View >
"""
for x in range(10):
    n = int(input())
    buildings = list(map(int, input().split()))
    checkPoint = [-2, -1, 1, 2]
    answer = 0
    for i in range(n):
        if buildings[i] == 0:
            continue
        
        jump = False
        max_building = 0
        for check in checkPoint:
            if buildings[i] < buildings[i + check]:
                jump = True
                break
            if buildings[i + check] > max_building:
                max_building = buildings[i + check]
        
        if jump:
            continue
        answer += buildings[i] - max_building

    print("#{} {}".format(x + 1, answer))