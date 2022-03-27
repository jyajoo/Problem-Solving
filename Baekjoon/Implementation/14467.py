'''
< 소가 길을 건너간 이유 1 >

- 소의 위치는 왼쪽0, 오른쪽1
- 소를 관측한 적이 있는 지 확인
- 기존에 관측한 적이 있다면, 위치 비교
'''

n = int(input())    # 관찰 횟수
cow = []
street = dict()
cnt = 0
for _ in range(n):  # (소의 번호, 소의 위치)
    c, s = map(int, input().split())
    if c not in cow:                   # 소를 관측한 적이 있는 지 확인
        cow.append(c)
    else:
        if street[c] != s:             # 관측한 적이 있다면, 위치 비교
            cnt += 1
    street[c] = s
print(cnt)