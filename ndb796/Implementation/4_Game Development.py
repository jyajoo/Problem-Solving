'''
< 게임 개발 >

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
