"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

< 농작물 수확하기 >
"""
T = int(input())

for t in range(T):
    n = int(input())
    numbers = [list(map(int, input())) for _ in range(n)]
    start = n // 2
    count = 1
    answer = 0

    x, y = 0, 0
    minus = True
    plus = True
    while True:
        for _ in range(count):
            answer += numbers[x][y + start]
            y += 1
        
        y = 0
        x += 1
        if minus:
            start -= 1
        else:
            start += 1

        if plus:
            count += 2
        else:
            count -= 2

        if start == 0:
            minus = False
        
        if count == n:
            plus = False

        if x == n:
            break
    print("#{} {}".format(t + 1, answer))
        
        

