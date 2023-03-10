-- 코드를 입력하세요
# SELECT DISTINCT CAR_ID, 
#     CASE
#         WHEN CAR_ID IN(
#             SELECT CAR_ID
#             FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#             WHERE DATE('2022-10-16') BETWEEN START_DATE AND END_DATE
#         ) THEN "대여중"
#         ELSE "대여가능"
#     END AS AVAILABILITY
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# ORDER BY CAR_ID DESC;


SELECT DISTINCT CAR_ID,
    CASE 
        WHEN CAR_ID IN (
            SELECT CAR_ID 
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
            WHERE DATE('2022-10-16') BETWEEN START_DATE AND END_DATE
        ) THEN '대여중'
        ELSE '대여 가능'
    END `AVAILABILITY`
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY 1 DESC;

# SELECT *
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE "2022-10-16" >= START_DATE AND "2022-10-16" <= END_DATE