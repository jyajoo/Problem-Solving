'''
< 기둥과 보 설치>


'''
frames = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [
    2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

build = []

def solution(n, frames):
    x = 0
    for frame in frames:
        if frame[3] == 1:
            if (frame[1] == 0
                or [frame[0] - 1, frame[1], 1] in build
                or [frame[0], frame[1] - 1, 0] in build
                or [frame[0] + 1, frame[1] - 1, 0] in build
                    or ([frame[0]-1, frame[1], 1] in build and [frame[0]+1, frame[1], 1] in build)):
                build.append([frame[0], frame[1], frame[2]])

        else:
            build.remove([frame[0], frame[1], frame[2]])
            if frame[2] == 1:
                if [frame[0]-1, frame[1], 1] in build:
                    if [frame[0]-1, frame[1]-1, 0] and [frame[0], frame[1], 0] not in build:
                        build.append([frame[0], frame[1], frame[2]])
                elif [frame[0]+1, frame[1], 1] in build:
                    if [frame[0] + 1, frame[1] - 1, 0] and [frame[0]+2, frame[1], 0] not in build:
                        build.append([frame[0], frame[1], frame[2]])
            else:
                for i in range(frame[0], n):
                    if [i, frame[1] + 1, 1] in build:
                        if [i, frame[1], 0] in build:
                            x += 1
                            break
                for i in range(0, frame[0]):
                    if [frame[0] - 1, frame[1] + 1, 1] in build:
                        if [frame[0] - 1, frame[1], 0] in build:
                            x += 1
                            break
                if x > 0:
                    build.append([frame[0], frame[1], frame[2]])

    build.sort(key=lambda x: (x[0], x[1], x[2]))
    return build


print(solution(len(frames), frames))
