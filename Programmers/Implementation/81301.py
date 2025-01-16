'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/81301

< 숫자 문자열과 영단어 >
'''
def solution(s):
    answer = ''
    num = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six': '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    ex = ''
    for i in s:
        ex += i
        if ex in num.keys():
            answer += num.get(ex)
            ex = ''
        if i.isdigit():
            answer += i
            ex = ''
            continue
    
    return int(answer)
