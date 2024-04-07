with source as (
      select * from {{ source('postgres', 'salesperson') }}
),
renamed as (
    select
        {{ adapter.quote("sales_person_id") }},
        {{ adapter.quote("name") }},
        {{ adapter.quote("age") }},
        {{ adapter.quote("gender") }},
        {{ adapter.quote("position") }},
        {{ adapter.quote("joining_date") }},
        {{ adapter.quote("salary") }}

    from source
)
select * from renamed
  