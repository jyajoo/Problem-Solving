/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/273710

< ROOT 아이템 구하기 >
*/
SELECT a.ITEM_ID, a.ITEM_NAME
FROM ITEM_INFO a
JOIN ITEM_TREE b ON a.ITEM_ID = b.ITEM_ID
AND PARENT_ITEM_ID IS NULL