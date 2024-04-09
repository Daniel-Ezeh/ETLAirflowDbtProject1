
WITH ss AS (
    SELECT
        quantity,
        COUNT(quantity) counts
    FROM {{ ref("base_postgres_sales") }}
    GROUP BY
        quantity
),

sp as (
    SELECT
        sales_person_id, 
        name, 
        position,
        gender
    FROM {{ ref("base_postgres_salesperson") }}
)

SELECT 
    *
FROM ss  
JOIN 
    sp ON sales_person_id = sales_person_id
GROUP BY 
    name,  
    counts
ORDER BY gender