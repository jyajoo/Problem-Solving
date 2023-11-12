"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWcPjEuKAFgDFAU4&categoryId=AWcPjEuKAFgDFAU4&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

< 정곤이의 단조 증가하는 수 >
"""
T = int(input())

def check(num):
    num = str(num)

    for i in range(1, len(num)):
        if int(num[i]) < int(num[i - 1]):
            return False
    return True


for x in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    answer = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            num = numbers[i] * numbers[j]

            if check(num):
                answer = max(answer, num)
    if answer == 0:
        answer = -1
    print("#{} {}".format(x + 1, answer))
