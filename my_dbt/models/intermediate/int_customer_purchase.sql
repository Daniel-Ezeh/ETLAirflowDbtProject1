WITH customers AS (
    SELECT 
        customer_id
        first_name,
        last_name,
        gender,
        country
    FROM {{ ref("base_postgres_customers") }}
),

sales AS (
    SELECT
        quantity,
        sale_date
    FROM {{ ref("base_postgres_sales") }}
),

product as (
    SELECT
        brand,
        model,
        color,
        memory,
        selling_price
    FROM {{ ref("base_postgres_products") }}
)

SELECT 
        c.customer_id
        c.first_name,
        c.last_name,
        c.gender,
        c.country,
        p.brand,
        p.model,
        p.color,
        p.memory,
        p.selling_price,
        s.quantity,
        s.sale_date
FROM customers c
    LEFT JOIN sales s
    ON c.customer_id = s.customer_id
    LEFT JOIN products p
    ON s.product_id = p.product_id
