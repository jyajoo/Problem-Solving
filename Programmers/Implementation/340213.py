'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/340213

< [PCCP 기출 문제] 1번 / 동영상 재생기 >
'''
def solution(video_len, pos, op_start, op_end, commands):
    # 시간을 초로 변환
    def time_to_second(time):
        minute, second = map(int, time.split(":")) 
        return minute * 60 + second
    
        
    # 현 위치가 op에 해당하는지 확인
    def check_op():
        nonlocal pos
        if op_start <= pos <= op_end:
            pos = op_end
            
    # 초를 시간으로 변환
    def second_to_time(second):
        miniute = second // 60
        second = second % 60
        return f"{miniute:02}:{second:02}"
    
    video_len = time_to_second(video_len)
    pos = time_to_second(pos)
    op_start = time_to_second(op_start)
    op_end = time_to_second(op_end)
    
    check_op()
    for cmd in commands:
        if cmd == 'next':
            pos += 10
            if pos + 10 > video_len:
                pos = video_len
        else:
            pos -= 10
            if pos < 0:
                pos = 0
        check_op()
    
    return second_to_time(pos)
    