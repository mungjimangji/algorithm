-- 코드를 입력하세요
# SELECT CAR_ID, COUNT(CAR_ID)
# FROM(
#     SELECT *
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE "2022-08-01" <= START_DATE AND "2022-10-31" >= END_DATE
#     ) MYASD
# GROUP BY CAR_ID;

# SELECT *
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE "2022-08-01" <= START_DATE AND "2022-10-31" >= END_DATE
# ORDER BY END_DATE DESC

# SELECT MONTH(START_DATE) as MONTH, CAR_ID, COUNT(*) as RECORDS
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY o
# WHERE CAR_ID IN (
#     SELECT CAR_ID 
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE MONTH(START_DATE) BETWEEN 8 AND 10
#     GROUP BY CAR_ID
#     HAVING COUNT(*) >= 5)
#     AND MONTH(START_DATE) BETWEEN 8 AND 10
# GROUP BY MONTH, CAR_ID
# HAVING COUNT(*) > 0
# ORDER BY MONTH, CAR_ID DESC;

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE MONTH(START_DATE) BETWEEN 8 AND 10
    GROUP BY CAR_ID
    HAVING COUNT(CAR_ID) >= 5)
GROUP BY MONTH(START_DATE), CAR_ID
HAVING COUNT(*) > 0 AND MONTH BETWEEN 8 AND 10
ORDER BY MONTH, CAR_ID DESC