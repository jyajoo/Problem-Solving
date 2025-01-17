'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/155652

< 둘만의 암호 >
'''
def solution(s, skip, index):
    answer = ''
    for i in s:
        num = ord(i)
        count = 0
        while count < index:
            num += 1
            if num > ord('z'):
                num = ord('a')
            if chr(num) not in skip:
                count += 1
        answer += chr(num)
    
    return answer