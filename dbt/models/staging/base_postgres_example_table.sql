with source as (
      select * from {{ source('postgres', 'example_table') }}
),
renamed as (
    select
        {{ adapter.quote("id") }},
        {{ adapter.quote("name") }},
        {{ adapter.quote("age") }}

    from source
)
select * from renamed
  