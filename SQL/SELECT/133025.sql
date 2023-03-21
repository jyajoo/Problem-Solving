/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/133025

< 과일로 만든 아이스크림 고르기 >

- TOTAL_ORDER이 3000 초과
- TOTAL_ORDER가 높은 순대로 나열
- INGREDIENT_TYPE = 'fruit_based'
*/

SELECT FLAVOR
FROM ICECREAM_INFO i
WHERE FLAVOR IN (
    SELECT FLAVOR 
    FROM FIRST_HALF 
    WHERE TOTAL_ORDER > 3000
    ORDER BY TOTAL_ORDER 
) 
AND INGREDIENT_TYPE = 'fruit_based'
