/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/131115

< 가격이 제일 비싼 식품의 정보 출력하기 >
*/
SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1

/**/
SELECT *
FROM FOOD_PRODUCT
WHERE PRICE = (
    SELECT MAX(PRICE)
    FROM FOOD_PRODUCT
)