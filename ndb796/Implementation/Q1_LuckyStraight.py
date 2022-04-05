'''
< 럭키 스트레이트 >

- 입력받은 점수를 반으로 나누어 좌우 계산 후 동일한지 확인
- 항상 짝수로 주어진다.
'''

score = input()
mid = len(score) // 2
left = right = 0

for i in range(mid):
    left += int(score[i])

for i in range(mid, len(score)):
    right += int(score[i])

if left == right:
    print("LUCKY")
else:
    print("READY")
