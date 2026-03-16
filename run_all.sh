#!/bin/bash

echo "Starting Data Pipeline..."

# 1. API se data fetch karna
python3 scripts/currency_bootstrap.py

# 2. Data clean aur transform karna
python3 src/transform.py

# 3. Snowflake mein load karna
python3 src/load_to_snowflake.py

echo "Pipeline executed successfully!"