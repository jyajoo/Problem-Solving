/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/301647

< 부모의 형질을 모두 가지는 대장균 찾기 >
*/
SELECT ed_1.ID, ed_1.GENOTYPE, ed_2.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA ed_1
JOIN ECOLI_DATA ed_2
ON ed_1.PARENT_ID = ed_2.ID
WHERE (ed_1.GENOTYPE & ed_2.GENOTYPE) = ed_2.GENOTYPE 
ORDER BY ed_1.ID