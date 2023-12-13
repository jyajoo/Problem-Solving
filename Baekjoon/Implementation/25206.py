"""
백준 - https://www.acmicpc.net/problem/25206

< 너의 평점은 >
"""
import sys

input = sys.stdin.readline
arr = []
grade_score = {"A+":4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0}
for _ in range(20):
    name, score, grade = input().split()
    arr.append((name, float(score), grade))

total_score = 0
total_grade = 0
for name, score, grade in arr:
    if grade != 'P':
        total_grade += grade_score.get(grade) * float(score)
        total_score += float(score)

print(total_grade / total_score)