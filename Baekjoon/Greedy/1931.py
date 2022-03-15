'''
< 회의실 배정 >

- 가장 빠르게 끝나는 회의, 가장 빠르게 시작하는 회의 순으로 정렬한다.
- 다음 회의의 시작 시간이 이전 회의의 끝나는 시간과 동일하거나 큰지 확인
'''

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

cnt = 0
time = 0

arr.sort(key = lambda x : (x[1], x[0]))

for x in arr:
    if (time <= x[0]):
        time = x[1]
        cnt += 1


print(cnt)

