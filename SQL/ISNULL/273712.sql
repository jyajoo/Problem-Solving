/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/273712

< 업그레이드 할 수 없는 아이템 구하기 >
*/
SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID NOT IN (
    SELECT PARENT_ITEM_ID
    FROM ITEM_TREE
    WHERE PARENT_ITEM_ID IS NOT NULL
                 )
ORDER BY ITEM_ID DESC