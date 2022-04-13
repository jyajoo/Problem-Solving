'''
< 기둥과 보 설치>


'''
frames = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
    1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [1, 1, 1, 0], [2, 1, 0, 1]]

build = []


def solution(n, frames):
    x = 0
    build = []

    for frame in frames:
        # 설치인 경우
        if frame[3] == 1:
            if frame[2] == 0:
                if (frame[1] == 0
                    or [frame[0], frame[1] - 1, 0] in build
                    or [frame[0] - 1, frame[1], 1] in build
                        or [frame[0], frame[1] + 1, 1] in build):
                    build.append([frame[0], frame[1], frame[2]])

            else:
                if ([frame[0], frame[1] - 1, 0] in build
                    or [frame[0] + 1, frame[1] - 1, 0] in build
                        or ([frame[0] - 1, frame[1], 1] and [frame[0] + 1, frame[1], 1] in build)):
                    build.append([frame[0], frame[1], frame[2]])

        # 삭제인 경우
        else:
            build.remove([frame[0], frame[1], frame[2]])

            # 보일 경우
            if frame[2] == 1:

                x = 0
                for i in range(frame[0], n):
                    if [i, frame[1], 1] in build:
                        if [i, frame[1] - 1, 0] in build or [i + 1, frame[1] - 1, 0] in build:
                            x += 1
                            break
                for i in range(frame[0] - 1, -1, -1):
                    if [i, frame[1], 1] in build:
                        if [i, frame[1] - 1, 0] in build or [i + 1, frame[1] - 1, 0] in build:
                            x += 1
                            break
                if x == 2:
                    build.append([frame[0], frame[1], frame[2]])

            # 기둥일 경우
            else:
                x = 0
                # 기둥으로부터 오른쪽 보 확인
                for i in range(frame[0], n):
                    if [i, frame[1] + 1, 1] in build:
                        # 보 아래에 기둥이 하나라도 있을 경우
                        if [i, frame[1], 0] in build or [i + 1, frame[1], 0] in build:
                            x += 1
                            break
                for i in range(frame[0] - 1, -1, -1):
                    if [i, frame[1] + 1, 1] in build:
                        if [i, frame[1], 0] in build or [i + 1, frame[1], 0] in build:
                            x += 1
                            break
                if x < 2:
                    build.append([frame[0], frame[1], frame[2]])

    build.sort(key=lambda x: (x[0], x[1], x[2]))
    return build

print(solution(len(frames), frames))
