"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

< 원재의 메모리 복구하기 >
"""
def change(x):
    global bits
    for i in range(x + 1, len(bits)):
        if bits[i] == 0:
            bits[i] = 1
        else:
            bits[i] = 0


T = int(input())
for t in range(T):
    bits = list(map(int, input()))
    answer = 0
    while True:
        if 1 not in bits:
            break
        if 0 not in bits:
            answer += 1
            break
        num = bits[-1]
        for i in range(len(bits) - 2, -1, -1):
            if num != bits[i]:
                change(i)
                answer += 1
                break
    print("#{} {}".format(t + 1, answer))