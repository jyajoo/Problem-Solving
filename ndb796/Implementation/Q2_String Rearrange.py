'''
< 문자열 재정렬 >

- 영어는 사전순, 숫자는 모두 더해서 출력
'''

s = input()
s = sorted(s)
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(s)
result = ""
x = 0

for i in s:
    if i in num:
        x += int(i)
    else:
        result += i

print(result + str(x))

'''
책에서의 풀이
- isalpha로 알파벳인지 확인한다.
- join으로 하나의 문자열로 이어준다.
'''
s = input()
result = []
value = 0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)
result.sort()
if value != 0:
    result.append(str(value))

print(''.join(result))