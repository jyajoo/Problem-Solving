'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/15008/lessons/121683

< [PCCP 모의고사 1] 1번 >

'''

def solution(input_string):
    answer = ''
    word = ''
    word_list = []

    for i in range(len(input_string)):
        if i == 0 or ex_string == input_string[i]:
            word += input_string[i]
            ex_string = input_string[i]
        else:
            word_list.append(word)
            word = ''
            word += input_string[i]
            ex_string = input_string[i]
    
    word_list.append(word)

    chk = 0
    word_list.sort()
    for i in word_list:
        if word_list.count(i) > 1:
            chk += 1
            if i[0] not in answer:
                answer += i[0]
        elif word_list.count(i) == 1:
            chk2 = 0
            for j in word_list:
                if i[0] in j:
                    chk2 += 1
            if chk2 > 1:
                chk += 1
                if i[0] not in answer:
                    answer += i[0]
    
    if chk == 0:
        return "N"
    return answer