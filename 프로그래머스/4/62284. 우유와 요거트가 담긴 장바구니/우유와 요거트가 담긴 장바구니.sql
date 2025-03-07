-- 코드를 입력하세요
SELECT CART_ID
FROM CART_PRODUCTS
GROUP BY CART_ID
HAVING COUNT(DISTINCT
            CASE
                WHEN NAME = 'Milk' THEN 1
                WHEN NAME = 'Yogurt' THEN 2
            END) = 2
ORDER BY CART_ID