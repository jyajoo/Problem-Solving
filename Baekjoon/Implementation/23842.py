import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

# 0 ~ 9까지 필요한 성냥의 수
numbers = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
plus = 4

answer = int(input())
flag = False
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for lst in combinations_with_replacement(number, 4):
    number1 = str(lst[0]) + str(lst[1])
    number2 = str(lst[2]) + str(lst[3])
    number3 = str(int(number1) + int(number2))
    if len(number3) == 1:
        number3 = '0' + number3
    if int(number3) > 99:
        continue

    result = plus
    for i in lst:
        result += numbers.get(i)

    for i in number3:
        result += numbers.get(int(i))

    if result == answer:
        flag = True
        print("{}+{}={}".format(number1, number2, number3))
        break

if not flag:
    print("impossible")