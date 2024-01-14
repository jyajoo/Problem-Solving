"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/92334

< 신고 결과 받기 >

- 여러 번 신고가 가능하지만, 1번만 적용된다.
- k번 이상 신고되면, 여태까지의 내용이 한꺼번에 발송되며 정지된다.
"""


def solution(id_list, reports, k):
    answer = []
    id_reports = []
    id = {}
    count = 0
    report_count = [0] * len(id_list)
    for i in id_list:
        id[i] = count
        # 유저 id, 유저가 신고한 id, 정지된 id
        id_reports.append((count, [], []))
        count += 1

    for report in reports:
        x, y = report.split()
        x, y = id[x], id[y]

        x_id, x_report, x_stop = id_reports[x]
        if y not in x_report:
            x_report += [y]
            report_count[y] += 1
        id_reports[x] = (x_id, x_report, x_stop)

    stop_list = []
    for i in range(len(report_count)):
        if report_count[i] >= k:
            stop_list.append(i)

    for id, report, stop in id_reports:
        for i in report:
            if i in stop_list:
                stop += [i]

    for _, _, stop in id_reports:
        answer.append(len(stop))

    return answer


# id_list = ["muzi", "frodo", "apeach", "neo"]
# reports = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# k = 2

id_list = ["con", "ryan"]
reports = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, reports, k))
