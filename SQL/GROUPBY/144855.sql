/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/144855

< 카테고리 별 도서 판매량 집계하기 >
*/
WITH NEW AS (
    SELECT BOOK_ID, SUM(SALES) AS BOOK_TOTAL_SALES
    FROM BOOK_SALES
    WHERE SALES_DATE LIKE '2022-01%'
    GROUP BY BOOK_ID
    ORDER BY BOOK_ID
)

SELECT CATEGORY, SUM(BOOK_TOTAL_SALES) AS TOTAL_SALES
FROM BOOK a
JOIN NEW b ON a.BOOK_ID = b.BOOK_ID
GROUP BY CATEGORY
ORDER BY CATEGORY