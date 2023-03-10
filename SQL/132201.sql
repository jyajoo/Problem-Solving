/*
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/132201

< 12세 이하인 여자 환자 목록 출력하기 >

- IFNULL(TLNO, 'NONE') : NULL이면 'NONE' 출력, 아니면 TLNO 그대로 출력
*/
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12
AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME