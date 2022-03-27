'''
< 잃어버린 괄호 >

- + 연산자로 묶어주어야 큰 값이 -되면서 값이 최소값이 나온다.
- SyntaxError 발생 -> 0으로 시작되는 수 고려
'''

s = input().split('-')        # - 연산자를 기준으로 나눈다.
num = []
for i in s:
    a = 0
    x = i.split('+')          # + 연산자로 나누고 더한다. 
    for j in x:
        a += int(j)
    num.append(a)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]          # 괄호 속 +연산자가 계산된 값들을 차례대로 - 해준다.
print(result)

'''
'''

s = input().split('-')
result = 0
for i in s[0].split('+'):
    result += int(i)
for i in s[1:]:
    result -= int(i)
print(result)

'''
'''

# s = input()

# num = s.split("-")               # - 연산자를 기준으로 나눈다.
# result = ""
# for i in num:
#     a = 0
#     if "+" in i:                  # + 연산자가 포함되어 있는 경우, +를 기준으로 나눈다.
#         i = i.split("+")
#         for j in i:
#             if j.startswith("0"):           # 0으로 시작한다면,0 이후의 수를 찾는다.
#                 for i in j:
#                     idx = j.index(i)
#                     if i != "0":
#                         idx = j.index(i)
#                         break
#                 j = j[idx:]
#             a += int(j)                     
#     else:                         # + 연산자가 포함되어 있지 않는 경우
#         if i.startswith("0"):     # 0으로 시작한다면,0 이후의 수를 찾는다.
#             for j in i:
#                 idx = i.index(i)
#                 if j != "0":
#                     idx = i.index(j)
#                     break
#             i = i[idx:]
#         a += int(i)

#     result += str(a)
#     result += "-"
# result += "0"             
# print(eval(result))
