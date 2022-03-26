'''
< 곱하기 혹은 더하기 >

- 모든 연산은 왼쪽에서부터 이루어진다는 가정
- 주어진 수가 0 또는 1이거나 result가 0 또는 1인 상태인 경우, 더하기  (EX, 1 X 2, 1 + 2)
- 그 외에는 모두 곱하는 것이 최대의 수를 구할 수 있는 방법이 된다.
'''

'''
!! 잘못된 풀이 !!
> if i == 0 or result == 0:  
1인 경우 더하기 연산을 해주어야 한다.
'''

s = input()
result = 0

for i in s:
    i = int(i)
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

print(result)

'''
'''
data = input()
result = int(data[0])  # 첫 번째 숫자 대입해두기

for i in range(1, len(data)): # 두 번째 숫자부터 시작
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
