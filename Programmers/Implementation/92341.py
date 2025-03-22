"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/92341

< 주차 요금 계산 >
"""

import math


def solution(fees, records):
    answer = []
    time_records = {}
    for record in records:
        time, car_num, move = record.split()
        h, m = map(int, time.split(":"))
        time = h * 60 + m
        if car_num not in time_records:
            time_records[car_num] = []

        if move == "IN":
            time_records[car_num].append((time, 0))
        else:
            time_records[car_num].append((time, 1))

    car_times = []
    for car_num in time_records.keys():
        start = 0
        total_time = 0
        for time, move in time_records[car_num]:
            if move == 0:
                start = time
            else:
                if start < time:
                    total_time += time - start
                else:
                    total_time += (23 * 60 + 59) - start + time

        if move == 0:
            total_time += (23 * 60 + 59) - start

        car_times.append((car_num, total_time))
    car_times.sort(key=lambda x: x[0])

    base_time, base_money, unit_time, unit_money = fees
    for i in range(len(car_times)):
        time = car_times[i][1]
        if time <= base_time:
            answer.append(base_money)
        else:
            answer.append(
                base_money + (math.ceil((time - base_time) / unit_time)) * unit_money
            )

    return answer


# 기본 시간, 기본 요금, 단위 시간, 단위 요금
fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

# fees = [120, 0, 60, 591]
# records = [
#     "16:00 3961 IN",
#     "16:00 0202 IN",
#     "18:00 3961 OUT",
#     "18:00 0202 OUT",
#     "23:58 3961 IN"
# ]

# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]

print(solution(fees, records))

"""
"""
from collections import defaultdict
import math


def solution(fees, records):
    time, fee, unit_time, unit_fee = fees
    cars = defaultdict(list)
    for record in records:
        time_record, car_num, enter = record.split()
        hour, minute = map(int, time_record.split(":"))
        cars[car_num].append(60 * hour + minute)

    result = []

    for car_num, record in cars.items():
        # 총 이용 시간 계산
        total_time = 0
        for i in range(0, len(record), 2):
            in_time = record[i]
            out_time = 23 * 60 + 59
            if i + 1 < len(record):
                out_time = record[i + 1]
            total_time += out_time - in_time

        # 요금 계산
        total_fee = fee  # 기본 요금
        total_time -= time  # 기본 시간 제외
        if total_time > 0:
            total_time = math.ceil(total_time / unit_time)
            total_fee += total_time * unit_fee

        result.append((car_num, total_fee))

    result.sort()
    return [i[1] for i in result]

'''
'''
from collections import defaultdict
def solution(fees, records):

    fee_list = defaultdict(int)
    in_list = dict()
    for record in records:
        time, car, type = record.split()
        if type == 'IN':
            in_list[car] = time
        else:
            in_time = in_list[car]
            in_hour, in_minute = map(int, in_time.split(':'))
            out_hour, out_minute = map(int, time.split(':'))
            use_time = (out_hour * 60 + out_minute) - (in_hour * 60 + in_minute)
            fee_list[car] += use_time
            del in_list[car]
    
    for car, in_time in in_list.items():
        in_hour, in_minute = map(int, in_time.split(':'))
        use_time = (23 * 60 + 59) - (in_hour * 60 + in_minute)
        fee_list[car] += use_time
    
    fee_list = list(fee_list.items())
    fee_list.sort()
    answer = []
    basic_time, basic_fee, unit_time, unit_fee = fees
    for (_, time) in fee_list:
        f = basic_fee
        if time > basic_time:
            t = int((time - basic_time) / unit_time)
            if (time - basic_time) % unit_time != 0:
                t += 1
            f += t * unit_fee
        answer.append(f)
    
    return answer