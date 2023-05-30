/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/59041

< 동명 동물 수 찾기 >
*/
SELECT NAME, COUNT(*) AS 'COUNT'
FROM ANIMAL_INS
GROUP BY NAME
HAVING NAME IS NOT NULL
AND COUNT(*) >= 2
ORDER BY NAME