'''
< 문자열 뒤집기 >

- 문자열을 그룹지어 나눈다.
- 1과 0 중에 그룹 수가 더 적은 횟수
'''

s = input()
cnt_one = 0
cnt_zero = 0
prev = ''      # 이전 값

for i in s:
    if prev != i:          # 이전 값과 다른지 확인
        if i== '0':        # 1이나 0의 그룹 수 추가
            cnt_zero += 1
        else:
            cnt_one += 1
    prev = i

print(min(cnt_one, cnt_zero))   # 1과 0의 그룹 수 중 적은 값 출력
