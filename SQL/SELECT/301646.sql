/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/301646

< 특정 형질을 가지는 대장균 찾기 >
*/
/*
GENOTYPE을 2진수로 표현했을 때,
2번 (0010)은 존재하지 않고,
1번 (0001)과 3번(0100)은 존재하는 것만 조회해야 한다.

2번(0010)은 2, 1번(0001)은 1, 3번(0100)은 4라는 10진수를 나타내고 있으며,
비트 연산자 &를 이용하여 비교하면 된다.
*/
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE GENOTYPE & 2 = 0 
AND (GENOTYPE & 1 != 0 OR GENOTYPE & 4 != 0)