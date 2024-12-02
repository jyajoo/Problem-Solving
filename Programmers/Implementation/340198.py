'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/340198#

< [PCCE 기출문제] 10번 / 공원 >
'''
def solution(mats, park):
    # 돗자리를 내림차순으로 정렬한다.
    mats.sort(reverse = True)
    answer = -1
    for i in range(len(park)):
        for j in range(len(park[0])):
            # 빈 공간을 발견하면, 돗자리를 펼칠 수 있는지 확인한다.
            if park[i][j] == "-1":
                
                for mat in mats:
                    flag = False
                    # 돗자리를 펼칠 수 있는지 확인한다
                    if i + mat <= len(park) and j + mat <= len(park[0]):
                        # 돗자리를 펼칠 수 있는 공간이 전부 빈 공간인지 확인한다.
                        for x in range(i, i + mat):
                            for y in range(j, j + mat):
                                if park[x][y] != "-1":
                                    flag = True
                                    break
                            if flag:
                                break
                        
                        # 빈공간이 하나도 없는 경우, 돗자리를 펼친다.
                        if not flag:
                            if mat > answer:
                                answer = mat
                                
                                # 만약 가장 큰 돗자리를 펼칠 수 있다면, 바로 return
                                if answer == mats[0]:
                                    return answer 
    return answer
                    