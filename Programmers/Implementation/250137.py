"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/250137

< [PCCP 기출문제] 1번 / 붕대 감기 >
"""


def solution(bandage, health, attacks):
    heal_time, heal, plus_heal = bandage

    current_health = health

    attacks.sort()
    ex_attack_time = 0
    for attack_time, attack in attacks:
        # 현재 공격 시간과 이전 공격 시간의 차이
        time = attack_time - ex_attack_time - 1
        if time < heal_time:
            current_health += time * heal
        else:
            plus_cnt = time // heal_time
            current_health += (plus_cnt) * plus_heal + (time) * heal

        current_health = min(health, current_health)
        print(time, current_health)

        # 이전 공격 차이 업데이트
        ex_attack_time = attack_time
        # 피해량만큼 체력 차감
        current_health -= attack
        # 만약 0 이하가 되면, -1로 반환
        if current_health <= 0:
            current_health = -1
            break

        print(current_health)
    return current_health
