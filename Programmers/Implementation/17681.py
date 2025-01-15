"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/17681

< [1차] 비밀지도 >
"""


def solution(n, arr1, arr2):
    def change(arr):
        n = []
        for i in arr:
            x = bin(i)[2:]

            if len(x) < len(arr):
                x = "0" * (len(arr) - len(x)) + x
            n.append(x)
        return n

    arr1 = change(arr1)
    arr2 = change(arr2)

    answer = []
    for i in range(len(arr1)):
        x = ""
        for j in range(len(arr1)):
            if arr1[i][j] == "1" or arr2[i][j] == "1":
                x += "#"
            else:
                x += " "
        answer.append(x)
    return answer


"""
"""


def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        x = bin(a | b)[2:]
        x = x.rjust(n, "0")
        x = x.replace("1", "#")
        x = x.replace("0", " ")
        answer.append(x)
    return answer
