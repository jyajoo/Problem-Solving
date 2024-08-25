"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/258712

< 가장 많이 받은 선물 >
"""

from collections import defaultdict
from itertools import combinations


def solution(friends, gifts):
    friend_give = defaultdict(list)
    friend_take = defaultdict(list)
    result = defaultdict(int)

    for gift in gifts:
        gift = gift.split()
        give, take = gift[0], gift[1]
        friend_give[give].append(take)
        friend_take[take].append(give)

    for a, b in combinations(friends, 2):
        a_give_cnt = friend_give[a].count(b)
        b_give_cnt = friend_give[b].count(a)

        if (a_give_cnt == 0 and b_give_cnt == 0) or a_give_cnt == b_give_cnt:
            # 선물 지수 비교
            a_present_point = len(friend_give[a]) - len(friend_take[a])
            b_present_point = len(friend_give[b]) - len(friend_take[b])

            if a_present_point != b_present_point:
                if a_present_point > b_present_point:
                    result[a] += 1
                else:
                    result[b] += 1

        else:
            if a_give_cnt > b_give_cnt:
                result[a] += 1
            else:
                result[b] += 1

    if len(result) == 0:
        return 0
    else:
        answer = 0
        for i in result.values():
            answer = max(answer, i)
        return answer
