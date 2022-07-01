'''
백준 - https://www.acmicpc.net/problem/23854

< The Battle of Giants >

'''

a_score = int(input())
b_score = int(input())

a_win = 0
draw = 0
b_win = 0

if a_score >=3:
  a_win += a_score // 3
  a_score = a_score % 3

if b_score >= 3:
  b_win += b_score // 3
  b_score = b_score % 3


if a_score == b_score:
  draw += a_score
  print(a_win, draw, b_win)

else:
  print(-1)
