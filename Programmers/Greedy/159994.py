'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/159994

< 카드 뭉치 >
'''
def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.remove(word)
        elif cards2 and word == cards2[0]:
            cards2.remove(word)
        else:
            return 'No'
    
    return 'Yes'