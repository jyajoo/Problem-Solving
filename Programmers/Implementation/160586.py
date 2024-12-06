'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/160586

< 대충 만든 자판 >
'''
def solution(keymap, targets):
    answer = []
    
    for target in targets:
        count = 0
        
        for i in target:
            min_idx = int(1e9)
            flag = False
            for key in keymap:
                if i in key:
                    min_idx = min(min_idx, key.index(i))
            if min_idx == int(1e9):
                count = -1
                break
            count += min_idx + 1
        answer.append(count)
                
        
    return answer