/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/131535

< 조건에 맞는 회원수 구하기 >
*/
SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE >= 20 AND AGE <= 29
AND JOINED LIKE '2021%'