'''
프로그래머스 - https://programmers.co.kr/learn/courses/30/lessons/60062

< 외벽 점검 >
- 브루트포스 알고리즘을 이용한다.
- 친구의 순서 경우의 수를 모두 구한다.
- 각 경우의 수가 취약한 지점을 모두 점검할 수 있는지 확인한다.
-
'''
from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1        
    length = len(weak)
    for i in range(length):       # 원형 형태의 weak를 2배로 늘려 직선 형태로 고려한다.
        weak.append(weak[i] + n)

    for start in range(length):   # weak의 시작점을 바꿔 모든 경우의 수 탐색
        for friends in list(permutations(dist, len(dist))):  # 친구의 순서를 고려하여 모든 경우의 수 탐색
            cnt = 1
            position = weak[start] + friends[cnt - 1]

            for index in range(start, start + length):
                if position < weak[index]:   # 모든 취약 지점을 점검하지 않은 경우
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[index] + friends[cnt - 1]   # position 재설정
            answer = min(answer, cnt)

    if answer > len(dist):
        return -1
    return answer

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

print(solution(n, weak, dist))
