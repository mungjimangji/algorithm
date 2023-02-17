-- 코드를 입력하세요
SELECT 
    HISTORY_ID, CAR_ID, date_format(START_DATE, '%Y-%m-%d') AS START_DATE, date_format(END_DATE, '%Y-%m-%d') AS END_DATE,
    CASE
        WHEN (DATEDIFF(END_DATE, START_DATE)+1) >= 30 THEN "장기 대여"
        ELSE "단기 대여"
    END AS RENT_TYPE
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE YEAR(START_DATE) = 2022 AND MONTH(START_DATE) = 9
ORDER BY
    HISTORY_ID DESC;