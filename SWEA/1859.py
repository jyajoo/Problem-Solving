"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc

< 백만 장자 프로젝트 >
"""
T = int(input())

for x in range(T):
    n = int(input())
    project = list(map(int, input().split()))

    answer = 0
    start = -1
    end = -1
    while start < n - 1:
        max_project = 0
        for i in range(end + 1, n):
            if project[i] > max_project:
                max_project = project[i]
                end = i

        for i in range(start + 1, end):
            answer += max_project - project[i]

        start = end

    print("#{} {}".format(x + 1, answer))

"""
"""
T = int(input())

for x in range(T):
    n = int(input())
    project = list(map(int, input().split()))

    answer = 0
    start = 0

    while start < n - 1:
        max_project = max(project[start:])
        max_index = project[start:].index(max_project) + start

        for i in range(start, max_index):
            answer += max_project - project[i]

        start = max_index + 1

    print("#%d %d" % (x + 1, answer))
"""
"""
T = int(input())

for x in range(T):
    n = int(input())
    project = list(map(int, input().split()))
    project = project[::-1]
    max_project = 0
    answer = 0
    for i in project:
        if i > max_project:
            max_project = i
        else:
            answer += max_project - i

    print("#%d %d" % (x + 1, answer))
