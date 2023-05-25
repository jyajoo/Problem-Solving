/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/133026

< 성분으로 구분한 아이스크림 총 주문량 >
*/
SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF fh
JOIN ICECREAM_INFO ii 
ON fh.FLAVOR = ii.FLAVOR
GROUP BY ii.INGREDIENT_TYPE