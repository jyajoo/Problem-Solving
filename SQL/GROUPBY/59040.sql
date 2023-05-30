/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/59040

< 고양이와 개는 몇 마리 있을까 > 
*/
SELECT ANIMAL_TYPE, COUNT(*) AS 'count'
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE