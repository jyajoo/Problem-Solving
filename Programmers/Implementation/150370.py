'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/150370#

< 개인정보 수집 유효기간 >
'''
from collections import defaultdict
def solution(today, terms, privacies):
    def validateDate(term, year, month, day):
        num_month = term_dict[term]
        
        month += num_month
        if month > 12:
            year += month // 12
            month %= 12
            if month == 0:
                month = 12
                year -= 1
        
        day -= 1
        if day == 0:
            day = 28
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        print(year, month, day)
        if tyear == year and tmonth == month:
            if tday > day:
                return False
            return True
                
        if tyear == year:
            if tmonth > month:
                return False
            return True
        
        if tyear > year:
            return False
        else:
            
            return True
    
    answer = []
    term_dict = defaultdict(int)
    for term in terms:
        alpha, num = term.split()
        term_dict[alpha] = int(num)
    
    tyear, tmonth, tday = map(int, today.split('.'))
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()
        year, month, day = map(int, date.split('.'))
        if not validateDate(term, year, month, day):
            answer.append(idx + 1)
    
    return answer
'''
'''
def solution(today, terms, privacies):
    answer = []
    tyear, tmonth, tday = map(int, today.split('.'))
    tday += tyear * 12 * 28 + tmonth * 28
    
    term_dict = {}
    for term in terms:
        alpha, num = term.split()
        term_dict[alpha] = int(num) * 28

    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()
        year, month, day = map(int, date.split('.'))
        day += year * 12 * 28 + month * 28
        
        day += term_dict[term]
    
        if tday >= day:
            answer.append(idx + 1)
        
    return answer