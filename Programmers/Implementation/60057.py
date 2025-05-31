"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/60057

< 문자열 압축 >
"""


def solution(s):
    answer = len(s)  # 압축되지 않을 시의 문자열 길이

    for step in range(1, len(s) // 2 + 1):  # 1부터 문자열 길이의 반까지 단위를 나누게 된다.
        prev = s[0:step]  # 비교가 이루어질 이전 문자열
        word = ""  # 최종적으로 압축된 문자열
        count = 1
        for i in range(step, len(s), step):  # 이전 for문에서의 단위마다 문자열을 나눌 수 있도록 한다.
            if prev == s[i : i + step]:  # 이전 문자열인 prev와 비교
                count += 1
            else:
                # count가 2 이상일 경우, count를 포함하여 압축된 문자열을 표현한다.
                word += str(count) + prev if count >= 2 else prev
                count = 1  # count 재설정
                prev = s[i : i + step]  # prev 재설정

        # 두번째 for문을 마치고 나서 남은 문자열을 덧붙여주어 마무리한다.
        word += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(word))

    return answer


s = "aabbaccc"
print(solution(s))

'''
'''
def solution(s):
    answer = len(s)
    
    for unit in range(len(s), 0, -1):
        ex_word, new_word = s[:unit], ''
        unit_cnt = 1
        result = ''

        for idx in range(unit, len(s), unit):
            new_word = s[idx:idx + unit]
            
            if ex_word == new_word:
                unit_cnt += 1
                
            elif ex_word != new_word:
                if unit_cnt > 1:
                    result += str(unit_cnt)
                    unit_cnt = 1
                result += ex_word
                ex_word = new_word

        if ex_word != new_word:
            result += ex_word
            result += new_word
        else:
            if unit_cnt > 1:
                result += str(unit_cnt)
            result += new_word
        answer = min(answer, len(result))
                
    return answer