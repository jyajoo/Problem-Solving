'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/72412

< 순위 검색 >
'''
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(infos, queries):
    # '-'로 취급할 조건 조합
    all_comb = []
    for i in range(5):
        comb = combinations([0, 1, 2, 3], i)
        all_comb.append(list(comb))
    
    # info로 만들 수 있는 조합을 key로, info 중 점수를 value로 설정한다.
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        for comb in all_comb:
            for c in comb:
                new_key = info[:-1]
                for idx in c:
                    new_key[idx] = '-'
                info_dict[''.join(new_key)].append(int(info[-1]))
    
    # 이진탐색을 위해 오름차순 정렬
    for val in info_dict.values():
        val.sort()
    
    # 쿼리를 key로, 점수를 bisect_left를 이용하여 위치를 찾는다
    # 이 위치를 이용하여 해당 점수보다 높은 지원자의 수를 도출한다.
    answer = []
    for query in queries:
        query = query.replace(" and ", "")
        query = query.split()
        key = query[0]
        val = int(query[1])
        
        idx = bisect_left(info_dict[key], val)
        answer.append(len(info_dict[key]) - idx)
    return answer
        