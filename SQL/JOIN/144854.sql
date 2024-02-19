/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/144854

< 조건에 맞는 도서와 저자 리스트 출력하기 >
*/
SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK a
JOIN AUTHOR b ON a.AUTHOR_ID = b.AUTHOR_ID
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE