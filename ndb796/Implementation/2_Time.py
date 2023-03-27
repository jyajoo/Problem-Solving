'''
< 시각 >

- 3이 하나라도 포함되어 있으면 수를 세는 것은
- 전체 경우의 수 - 3이 하나도 포함되지 않는 경우 를 구하면 된다.
'''
n = int(input())
all = (n + 1) * 60 * 60   # 전체 경우의 수
cnt = 0
for i in range(n):
    if '3' in str(i):
        cnt += 1          # 주어진 수까지 3이 포함되는 경우의 수

result = all - ((n + 1) - cnt) * 45 * 45   # 59초까지 3이 포함되지 않는 경우의 수는 45
print(result)


'''
- 완전 탐색(Brute Forcing)
- 확인(탐색)해야 할 전체 데이터의 개수가 100만 개 이하일 때 완전 탐색 이용
'''
h = int(input())
cnt = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)


'''
2023.03.27
'''
n = int(input())
result = 0

for i in range(n + 1):
    if i == 3:
        result += 60 * 60
    else:
        result += 15 * 60 + 45 * 15

print(result)