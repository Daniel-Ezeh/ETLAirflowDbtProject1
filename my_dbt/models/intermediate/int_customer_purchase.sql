{{ confi }}

WITH cc AS (
    SELECT 
        customer_id,
        first_name,
        last_name,
        gender,
        country
    FROM {{ ref("base_postgres_customers") }}
    ORDER BY gender ASC
),

ss AS (
    SELECT
        quantity,
        sale_date
    FROM {{ ref("base_postgres_sales") }}
),

pp as (
    SELECT
        product_id,
        brand,
        model,
        color,
        memory,
        selling_price
    FROM {{ ref("base_postgres_products") }}
)

SELECT 
        cc.customer_id,
        cc.first_name,
        cc.last_name,
        cc.gender,
        cc.country,
        pp.brand,
        pp.model,
        pp.color,
        pp.memory,
        pp.selling_price,
        ss.quantity,
        ss.sale_date
FROM ss  JOIN 
    cc ON cc.customer_id = customer_id
JOIN 
    pp ON pp.product_id = product_id
    ORDER BY gender

