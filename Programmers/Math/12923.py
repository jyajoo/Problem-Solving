'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12923

< 숫자 블록 >
'''
def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        val = 1
        if i == 1:
            val = 0
        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    val = max(val, j)
                    if i // j <= 10000000:
                        val = max(val, i // j)
                        break
        
        answer.append(val)
        
    return answer