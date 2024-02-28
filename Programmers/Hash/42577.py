'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42577

< 전화번호 목록 >
'''

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                return False
    return True

'''
'''
def solution(pb):
    pb.sort()
    for i, j in zip(pb, pb[1:]):
        if j.startswith(i):
            return False
    return True


'''
'''
def solution(pb):
    hash = {}
    for i in pb:
        hash[i] = 1
    for i in pb:
        temp = ""
        for j in i:
            temp += j
            if temp in hash and temp != i:
                return False
    return True
'''
'''
def solution(phone_book):
    answer = True

    books = {}
    l = set()
    for i in phone_book:
        l.add(len(i))

    for i in phone_book:
        for j in l:
            if len(i) >= j:
                if i[:j] not in books:
                    books[i[:j]] = 1
                else:
                    books[i[:j]] += 1

    for i in phone_book:
        if books[i] > 1:
            answer = False

    return answer
