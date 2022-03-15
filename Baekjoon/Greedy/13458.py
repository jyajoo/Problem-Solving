'''
< 시험 감독 >

- 시험장 개수만큼 총 감독관 추가
- 감시당하지 않는 응시자 수(i)에 따라 부감독관 추가
    - i가 부감독관의 응시자 감시 한계수보다 큰 경우와, 작거나 0인 경우
'''
n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())   # 총감독관, 부감독관의 응시자 감시 한계

result = n
for i in arr:
    i -= b
    if i > c:                # 남은 응시자 수가 부감독관의 응시자 감시 한계보다 큰 경우
        result += i // c     # 부감독관의 수를 더해주고, 응시자 수에서 감시되는 응시자 수를 뺀다.
        i -= (i // c) * c
        if i > 0:            # 감시당하지 않는 응시자 수가 남아있다면, 부감독관 한 명 더 추가
            result += 1

    elif i > 0 and i <= c:   # 부감독관의 응시자 감시 한계보다 적은 경우, 부감독관 한 명으로 충분
        result += 1

print(result)

'''
- 부감독관의 감시 한계로 나눠떨어지는지 확인
    - 나눠떨어지지 않고, 부감독관의 감시 한계보다 크다면, 나머지를 고려하여 한 명 더 추가
    - 작으면, 한 명만 추가
'''
n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())   # 총감독관, 부감독관의 응시자 감시 한계

result = n

for i in arr:
    i -= b
    if i < 0:       # 음수가 되지는 않는지 확인해주어야 한다..!!
        continue

    if i % c == 0:
        result += i // c
    else:
        if i > c:
            result += (i // c) + 1
        else:
            result += 1

print(result)

'''
- 감시당하지 않는 응시자가 0보다 큰지 확인
- 나머지가 존재한다면 부감독관 한 명 추가
'''
n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())   # 총감독관, 부감독관의 응시자 감시 한계

result = n

for i in arr:
    i -= b
    if i > 0:
        result += i // c
        if i % c > 0:
            result += 1

print(result)
