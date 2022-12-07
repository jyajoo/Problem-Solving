'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/15007/lessons/121682

< [PCCE 모의고사 2] 10번 >

'''

def solution(n, board, positions):
    answer = []
    num = [-1, 0, 1]
    
    for position in positions:
        chk = 0
        for i in num:
            for j in num:
                if i == 0 and j == 0:
                    continue
                if position[0] + i >= len(board) or position[1] + j >= len(board[0]) or position[0] + i < 0 or position[1] + j < 0:
                    continue
                if board[position[0] + i][position[1] + j] == 1:
                    chk += 1
                    
        if board[position[0]][position[1]] == 1:
            if chk <= 2 or chk >= 5:
                answer.append(0)
            else:
                answer.append(1)
                
        else:
            if chk == 2:
                answer.append(1)
            else:
                answer.append(0)
        
    return answer