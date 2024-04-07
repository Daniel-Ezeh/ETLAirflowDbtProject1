with source as (
      select * from {{ source('postgres', 'products') }}
),
renamed as (
    select
        {{ adapter.quote("product_id") }},
        {{ adapter.quote("brand") }},
        {{ adapter.quote("model") }},
        {{ adapter.quote("color") }},
        {{ adapter.quote("memory") }},
        {{ adapter.quote("storage") }},
        {{ adapter.quote("rating") }},
        {{ adapter.quote("selling_price") }}

    from source
)
select * from renamed
  