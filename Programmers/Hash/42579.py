"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42579

< 베스트앨범 > 
"""


def solution(genres, plays):
    answer = []
    music = {}
    play_rank = {}
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if genre not in music:
            music[genre] = [(i, play)]
            play_rank[genre] = play
        else:
            music[genre].append((i, play))
            play_rank[genre] += play

    play_rank = sorted(play_rank.items(), key=lambda x: -x[1])

    for genre, _ in play_rank:
        music[genre] = sorted(music[genre], key=lambda x: (-x[1], x[0]))
        answer.append(music[genre][0][0])
        if len(music[genre]) >= 2:
            answer.append(music[genre][1][0])

    return answer
