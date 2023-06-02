/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/59412

< 입양 시각 구하기(1) >
*/
SELECT HOUR(DATETIME), COUNT(*) AS 'COUNT'
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)