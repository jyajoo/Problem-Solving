'''
< 게임 개발 >

- 바라보는 방향에 따라 회전 방향 정하기
- 회전시켜가며 다음으로 이동할 수 있는지 확인
- 이동하고, 모든 방향 이동할 수 없다면 뒤로 이동하기
- 뒤로 이동하지 못할 경우, 멈추기
'''

n, m = map(int, input().split())
a, b, d = map(int, input().split())

place = []
for _ in range(n):
    place.append(list(map(int, input().split())))

# 다녀간 곳인지 확인
check = place
check[a][b] = 'c'

'''
[way]
바라보고 있는 방향이 
북이라면,  서남동북
동이라면, 북서남동
남이라면, 동북서남
서라면, 남동북서 순으로 회전
[step]
바라보고 있는 방향에 따른 이동 방향
[fail_step]
바라보고 있는 방향의 반대 이동 방향
'''
# 북0, 동1,남2, 서3
way = [(3, 2, 1, 0), (0, 3, 2, 1), (1, 0, 3, 2), (2, 1, 0, 3)]
step = [(-1, 0), (0, 1), (1, 0), (0, -1)]
fail_step = [(1, 0), (0, -1), (-1, 0), (0, 1)]

result = 1

while True:
    cnt = 0 # 4 방향 모두 못가는 경우
            # 바라보고 있는 방향에 따라 회전 방향 정하기
    for i in way[d]:
        na = a + step[i][0]
        nb = b + step[i][1]
                    # 벗어나는지, 바다인지, 이미 다녀온 곳인지 확인
        if na < 0 or na > n or nb < 0 or nb > m or place[na][nb] == 1 or check[na][nb] == 'c':
            cnt += 1
            continue
        else:        
            a = na
            b = nb
            result += 1
            check[a][b] = 'c'
            d = i
            # print(a, b, d)
            break
    
    # 4 방향 모두 갈 수 없는 경우, 한 칸 뒤로 이동
    if cnt == 4:
        na = a + fail_step[d][0]
        nb = b + fail_step[d][1]
        if na < 0 or na > n or nb < 0 or nb > m or place[na][nb] == 1:
            break
        else:
            a = na
            b = nb
            # print(a, b, d)

print(result)


'''
- 방문한 곳은 따로 c로 확인해줬었는데, 바다인 1로 표현해주어도 된다.
- 왼쪽 회전의 way[]를 함수로 표현
- 맵의 외곽은 모두 바다로 주어지므로 벗어나는지 확인할 필요가 없다.
'''

n, m = map(int, input().split())
a, b, d = map(int, input().split())

check = [[0] * m for _ in range(n)]
check[a][b] = 1   # 현재 좌표 방문 처리

place = []
for i in range(n):
    place.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 시뮬레이션 시작
result = 1
turn_time = 0

while True:
    turn_left()
    na = a + da[d]
    nb = b + db[d]
    if check[na][nb] == 0 and place[na][nb] == 0:  # 방문하지 않았고, 육지라면
        check[na][nb] = 1
        a = na
        b = nb
        result += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        na = a - da[d]
        nb = b - db[d]
        if place[a][b] == 0:
            a = na
            b = nb
        else:
            break
        turn_time = 0
print(result)