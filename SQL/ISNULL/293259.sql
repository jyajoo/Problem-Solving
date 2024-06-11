/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/293259

< 잡은 물고기의 평균 길이 구하기 >
*/
SELECT ROUND(AVG(LENGTH), 2) AS AVERAGE_LENGTH
FROM (
    SELECT IF (LENGTH IS NULL, 10, LENGTH) AS LENGTH
    FROM FISH_INFO
) AS LENGTH_TABLE
