/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/164673

< 조건에 부합하는 중고거래 댓글 조회하기 >
*/
-- 코드를 입력하세요
SELECT TITLE, b.BOARD_ID, REPLY_ID,
r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_REPLY r
WHERE DATE_FORMAT(b.CREATED_DATE, '%Y-%m') = '2022-10'
AND b.BOARD_ID = r.BOARD_ID
ORDER BY r.CREATED_DATE, TITLE