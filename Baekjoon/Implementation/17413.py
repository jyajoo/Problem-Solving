'''
백준 - https://www.acmicpc.net/problem/17413

< 단어 뒤집기 2 >
'''
import sys

input = sys.stdin.readline

n = input().strip()

answer = ''
flag = False
word = ''
for i in n:
    if i != '<' and not flag:
        word += i

    if i == '<':
        flag = True
        word_list = word.split()
        for w in range(len(word_list)):
            word_list[w] = word_list[w][::-1]
        answer += ' '.join(word_list)
        word = ''
    elif i == '>':
        answer += i
        flag = False

    if flag:
        answer += i

if len(word) != 0:
    word_list = word.split()
    for w in range(len(word_list)):
        word_list[w] = word_list[w][::-1]
    answer += ' '.join(word_list)
print(answer)     
