'''
< 곱하기 혹은 더하기 >

- 모든 연산은 왼쪽에서부터 이루어진다는 가정
- 주어진 수가 0이거나 result가 0인 상태인 경우, 더하기 
- 그 외에는 모두 곱하는 것이 최대의 수를 구할 수 있는 방법이 된다.
'''

s = input()
result = 0

for i in s:
    i = int(i)
    if i == 0 or result == 0:
        result += i
    else:
        result *= i

print(result)


''''''

s = input()
result = 0

for i in range(len(s)):
    if i == 0 or result == 0:
        result = int(s[i])
    elif s[i] == 0:
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)
