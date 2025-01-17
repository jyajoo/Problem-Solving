"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/250135

< 아날로그 시계 >
"""


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    # 시작시간과 끝시간을 초단위로 변환
    start = h1 * 60 * 60 + m1 * 60 + s1
    end = h2 * 60 * 60 + m2 * 60 + s2

    # 시작시간 00시, 12시라면, 초침이 시침/분침과 겹친다.
    # 이 때 알람은 단 한 번만 울린다.
    if start == 0 or start == 12 * 60 * 60:
        answer += 1

    # 시침은 1시간에 30도 이동, 1분에 0.5도 이동, 1초에 1/120도 이동
    # 분침은 1분에 6도 이동, 1초에 0.1도 이동
    # 초침은 1초에 6도 이동
    while start < end:
        # 현재 초침, 분침, 시침의 각도
        hAngle = (start / 120) % 360
        mAngle = (start / 10) % 360
        sAngle = (start * 6) % 360

        # 1초가 지난 후 각도, 0도가 되는 건 360도로 표현
        if ((start + 1) / 120) % 360 == 0:
            hNextAngle = 360
        else:
            hNextAngle = ((start + 1) / 120) % 360

        if ((start + 1) / 10) % 360 == 0:
            mNextAngle = 360
        else:
            mNextAngle = ((start + 1) / 10) % 360

        if ((start + 1) * 6) % 360 == 0:
            sNextAngle = 360
        else:
            sNextAngle = ((start + 1) * 6) % 360

        # 1초 후에 초침이 시침을 지나가는 경우
        if sAngle < hAngle and sNextAngle >= hNextAngle:
            answer += 1
        # 1초 후에 초침이 분침을 지나가는 경우
        if sAngle < mAngle and sNextAngle >= mNextAngle:
            answer += 1

        # 1초 후에 초침이 시침/분침을 동시에 지나가는 경우
        if sNextAngle == hNextAngle and hNextAngle == mNextAngle:
            answer -= 1

        start += 1
    return answer
