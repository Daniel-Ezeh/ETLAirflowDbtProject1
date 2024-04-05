with source as (
      select * from {{ source('postgres', 'customers') }}
),
renamed as (
    select
        {{ adapter.quote("customer_id") }},
        {{ adapter.quote("first_name") }},
        {{ adapter.quote("last_name") }},
        {{ adapter.quote("email") }},
        {{ adapter.quote("phone") }},
        {{ adapter.quote("address") }},
        {{ adapter.quote("country") }}

    from source
)
select * from renamed
  