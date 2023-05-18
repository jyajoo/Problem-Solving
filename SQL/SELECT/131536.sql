/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/131536

< 재구매가 일어난 상품과 회원 리스트 구하기 >
*/
-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(PRODUCT_ID) >= 2
ORDER BY USER_ID, PRODUCT_ID DESC