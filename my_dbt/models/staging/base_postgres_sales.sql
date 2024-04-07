with source as (
      select * from {{ source('postgres', 'sales') }}
),
renamed as (
    select
        {{ adapter.quote("sale_id") }},
        {{ adapter.quote("customer_id") }},
        {{ adapter.quote("sales_person_id") }},
        {{ adapter.quote("product_id") }},
        {{ adapter.quote("quantity") }},
        {{ adapter.quote("sale_date") }}

    from source
)
select * from renamed
  