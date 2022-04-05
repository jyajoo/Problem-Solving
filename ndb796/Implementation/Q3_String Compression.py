'''
프로그래머스 - https://programmers.co.kr/learn/courses/30/lessons/60057

< 문자열 압축 >

- 런타임 에러 문자열이 하나만 입력되는 경우를 고려하지 않음.
'''

s = input()
answer = []

def min_val(arr):
    prev = arr[0]
    cnt = 1
    result = ""
    for i in range(1, len(arr)):
        if prev == arr[i]:
            cnt += 1
        else:
            if cnt > 1:
                result += str(cnt) + prev
            else:
                result += prev
            cnt = 1
            prev = arr[i]
    if cnt > 1:
        result += str(cnt) + prev
    else:
        result += prev
    answer.append(len(result))

def solution(s):
    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2 + 1):
        # i(단위)만큼 묶어서 리스트 만들기
        arr = []
        couple = ''
        left = 0
        right = i
        for j in range(len(s)//i):
            couple = s[left:right]
            arr.append(couple)
            left = right
            right += i
        if len(s) % i != 0:
            arr.append(s[left:])
        min_val(arr)

    return min(answer)

print(solution(s))
