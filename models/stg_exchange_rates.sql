{{ config(materialized='table') }}

SELECT
    CURRENCY,
    RATE,
    TIMESTAMP
FROM {{ source('raw_data', 'EXCHANGE_RATES') }}
