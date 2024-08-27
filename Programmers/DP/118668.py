"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/118668?language=python3

< 코딩 테스트 공부 >
"""


def solution(alp, cop, problems):
    max_alp_req = max_cop_req = 0

    for alp_req, cop_req, _, _, _ in problems:
        max_alp_req = max(max_alp_req, alp_req)
        max_cop_req = max(max_cop_req, cop_req)

    # 이미 주어진 alp, cop이 최대인 경우일 수도 있음
    max_alp = max(alp, max_alp_req)
    max_cop = max(cop, max_cop_req)

    # dp[i][j] : alp = i, cop = j로 도달할 때까지 걸리는 최소 시간
    dp = [[int(1e9)] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 알고력, 코딩력 공부하기
            if i < max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    ni = min(max_alp, i + alp_rwd)
                    nj = min(max_cop, j + cop_rwd)
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + cost)

    return dp[max_alp][max_cop]