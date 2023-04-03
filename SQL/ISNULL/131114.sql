/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/131114

< 경기도에 위치한 식품창고 목록 출력하기 >
*/
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N')
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'