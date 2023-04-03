/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/59405

< 상위 n개 레코드 >
*/
SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME 
= (
    SELECT MIN(DATETIME)
    FROM ANIMAL_INS
)