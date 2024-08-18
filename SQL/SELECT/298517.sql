/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/298517

< 가장 큰 물고기 10마리 구하기 >
*/
SELECT ID, LENGTH
FROM FISH_INFO 
WHERE LENGTH IS NOT NULL 
ORDER BY LENGTH DESC, ID
LIMIT 10