'''
< 잃어버린 괄호 >

- eval() 함수는 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
- + 연산자로 묶어주어야 크게 -되면서 값이 최소값이 나온다.
- SyntaxError 발생 -> 0으로 시작되는 수 고려
'''
from itertools import permutations
s = input()

num = s.split("-")
result = ""
for i in num:
    a = 0
    if "+" in i:
        i = i.split("+")
        for j in i:
            if j.startswith("0"):
                for i in j:
                    idx = j.index(i)
                    if i != "0":
                        idx = j.index(i)
                        break
                j = j[idx:]
            a += int(j)
    else:
        if i.startswith("0"):
            for j in i:
                idx = i.index(i)
                if j != "0":
                    idx = i.index(j)
                    break
            i = i[idx:]
        a += int(i)

    result += str(a)
    result += "-"
result += "0"
print(eval(result))
