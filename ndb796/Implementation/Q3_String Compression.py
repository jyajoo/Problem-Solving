'''
프로그래머스 - https://programmers.co.kr/learn/courses/30/lessons/60057

< 문자열 압축 >

- 런타임 에러 (문자열이 하나만 입력되는 경우를 고려하지 않음.)
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

    for i in range(1, len(s)//2 + 1): # 단위는 1에서 len(s)//2까지 가능하다.
        arr = []
        couple = ''
        left = 0
        right = i
        for j in range(len(s)//i):    # len(s) // 단위 만큼 반복하여 문자열을 단위만큼 나눠 묶는다.
            couple = s[left:right]
            arr.append(couple)
            left = right
            right += i

        if len(s) % i != 0:           # 단위로 나눠떨어지지 않는 경우, 남아버린 문자열을 묶어버린다.
            arr.append(s[left:])

        min_val(arr)

    return min(answer)


print(solution(s))

'''

- 리스트 슬라이싱, 초깃값:최댓값:증감값 이용하기
- ''를 추가해주어 남은 문자열을 처리하는 if 문을 줄일 수 있도록 한다.
- 리스트 컴프리헨션 사용
'''
s = input()

def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):                     # 단위는 1에서 len(s)//2까지 가능하다.
        arr = [s[j : j + step] for j in range(0, len(s), step)]       # 단위만큼 문자열을 나눈다.
        arr.append('')
        prev = arr[0]
        cnt = 1
        length = 0
        for j in range(1, len(arr)):
            if prev == arr[j]:
                cnt += 1
            else:
                length += len(prev) + (len(str(cnt)) if cnt > 1 else 0)
                prev = arr[j]
                cnt = 1
        # answer = (length if answer > length else answer)
        answer = min(answer, length) 
    return answer

print(solution(s))


'''
책에서의 코드

'''
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j : j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer