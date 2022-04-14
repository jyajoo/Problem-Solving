'''
프로그래머스 - https://programmers.co.kr/learn/courses/30/lessons/60061

< 기둥과 보 설치>

- 런타임 에러, 아무래도 설치물이 규칙에 맞는지 확인해주는 함수를 따로 생성해주어야 할 것 같다. (갈아엎기)
'''

frames = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]


def rules(answer):
    for x, y, a in answer:
        # 구조물이 기둥인 경우
        if a == 0:
            if not (y == 0                # 1. 바닥 위어야 한다.
                    or [x - 1, y, 1] in answer    # 2. 보의 한 쪽 끝부분 위이여야 한다.
                    or [x, y, 1] in answer
                    or [x, y - 1, 0] in answer):  # 3. 다른 기둥 위여야 한다.
                return False

        # 구조물이 보인 경우
        else:
            if not([x, y - 1, 0] in answer  # 1. 한쪽 끝부분이 기둥 위어야 한다.
                    or [x + 1, y - 1, 0] in answer
                    or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)):   # 2. 양쪽 끝 부분이 다르 보들과 동시 연결되어야 한다.
                return False
    return True


def solution(n, frames):
    answer = []
    for frame in frames:
        # 구조물 설치
        if frame[3] == 1:
            answer.append([frame[0], frame[1], frame[2]])
            if rules(answer) == False:
                answer.pop()
        else:
            answer.remove([frame[0], frame[1], frame[2]])
            if rules(answer) == False:
                answer.append([frame[0], frame[1], frame[2]])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer


print(solution(len(frames), frames))
