'''
< 시각 > - refine

- 3이 하나라도 포함되어 있으면 수를 세는 것은
- 전체 경우의 수 - 3이 하나도 포함되지 않는 경우 를 구하면 된다.
'''
n = int(input())
all = (n + 1) * 60 * 60
cnt = 0
for i in range(n):
    if '3' in str(i):
        cnt += 1

result = all - ((n + 1) - cnt) * 45 * 45
print(result)
