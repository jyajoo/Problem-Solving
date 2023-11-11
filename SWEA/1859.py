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
            answer += (max_project - project[i])

        start = end

    print("#{} {}".format(x + 1, answer))
