-- 코드를 입력하세요
SELECT ID, NAME, L.HOST_ID
FROM PLACES L
INNER JOIN (
    SELECT HOST_ID, COUNT(HOST_ID)
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(HOST_ID) >= 2) R
ON L.HOST_ID = R.HOST_ID
ORDER BY ID;