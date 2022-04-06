'''
프로그래머스 - https://programmers.co.kr/learn/courses/30/lessons/60057

< 문자열 압축 >

- 런타임 에러 문자열이 하나만 입력되는 경우를 고려하지 않음.
'''

# s = input()
# answer = []


# def min_val(arr):
#     prev = arr[0]
#     cnt = 1
#     result = ""
#     for i in range(1, len(arr)):
#         if prev == arr[i]:
#             cnt += 1
#         else:
#             if cnt > 1:
#                 result += str(cnt) + prev
#             else:
#                 result += prev
#             cnt = 1
#             prev = arr[i]
#     if cnt > 1:
#         result += str(cnt) + prev
#     else:
#         result += prev
#     answer.append(len(result))


# def solution(s):
#     if len(s) == 1:
#         return 1

#     for i in range(1, len(s)//2 + 1): # 단위는 1에서 len(s)//2까지 가능하다.
#         arr = []
#         couple = ''
#         left = 0
#         right = i
#         for j in range(len(s)//i):    # len(s) // 단위 만큼 반복하여 문자열을 단위만큼 나눠 묶는다.
#             couple = s[left:right]
#             arr.append(couple)
#             left = right
#             right += i

#         if len(s) % i != 0:           # 단위로 나눠떨어지지 않는 경우, 남아버린 문자열을 묶어버린다.
#             arr.append(s[left:])

#         min_val(arr)

#     return min(answer)


# print(solution(s))

'''
단위만큼 묶어서 arr을 구성하는 방법

- 리스트 슬라이싱, 초깃값:최댓값:증감값 이용하기
'''
s = input()

for i in range(1, len(s) // 2):  # 단위는 1에서 len(s)//2까지 가능하다.
    arr = [s[j:j+i] for j in range(0, len(s), i)]
    print(arr)
