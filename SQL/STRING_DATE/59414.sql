/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/59414

< DATETIME에서 DATE로 형 변환 >
*/
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
