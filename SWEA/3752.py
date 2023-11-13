"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AWHPkqBqAEsDFAUn&categoryId=AWHPkqBqAEsDFAUn&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1

< 가능한 시험 점수 >
"""

T = int(input())

for t in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))

    result = [0]
    temp = [0]
    for i in range(n):
        for val in result:
            print(numbers[i], val)
            temp.append(numbers[i] + val)
        result = list(set(temp))
    print(result)
    print("#{} {}".format(t + 1, len(result)))


