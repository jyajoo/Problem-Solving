"""
SWEA -  https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

< [S/W 문제해결 기본] 1일차 - Flatten >
"""
for x in range(10):
    dump_chance = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump_chance):
        max_height = max(boxes)
        max_idx = boxes.index(max_height)
        min_height = min(boxes)
        min_idx = boxes.index(min_height)

        boxes[max_idx] -= 1
        boxes[min_idx] += 1
    print("#{} {}".format(x + 1, max(boxes) - min(boxes)))
