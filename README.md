# 🚀 Currency Exchange Data Pipeline

This project implements an automated **ETL data pipeline** that fetches real-time currency exchange rates from an API, processes the data, and loads it into a data warehouse.

The pipeline demonstrates a **modern Data Engineering workflow** including ingestion, transformation, orchestration, and infrastructure management.

---

# 📊 Architecture

The pipeline follows a layered architecture:

API → Data Ingestion → Data Cleaning → Data Warehouse

### Layers

**Bronze Layer (Raw Data)**

* Fetch currency exchange rates from the API
* Store raw data

**Silver Layer (Processed Data)**

* Clean and transform data using Python
* Handle missing values and formatting

**Gold Layer (Analytics Ready)**

* Load cleaned data into the warehouse
* Ready for analytics and dashboards

---

# ⚙️ Tech Stack

This project uses the following technologies:

* Python
* Pandas
* Snowflake
* dbt
* Terraform
* GitHub Actions

---

# 📁 Project Structure

```
ACEP_Project
│
├── .github/workflows/     # CI/CD pipelines
├── analyses/              # Data analysis files
├── config/                # Configuration files
├── data/                  # Raw and processed data
├── dbt_project/           # dbt models and configurations
├── macros/                # dbt macros
├── models/                # dbt transformation models
├── scripts/               # Data ingestion scripts
│   └── currency_bootstrap.py
│
├── src/                   # Core pipeline logic
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── load_cleaned.py
│   ├── load_to_snowflake.py
│   └── test_snowflake.py
│
├── terraform/             # Infrastructure-as-Code
│   └── main.tf
│
├── tests/                 # Test files
│
├── .env                   # Environment variables
├── .gitignore
├── dbt_project.yml
├── run_all.sh             # Pipeline orchestration script
└── README.md
```

---

# 🔄 Data Pipeline Workflow

The pipeline runs in the following steps:

### 1️⃣ Data Extraction

Fetch currency exchange rates from the API.

### 2️⃣ Data Transformation

Clean and transform the data using Python and Pandas.

### 3️⃣ Data Loading

Load the processed data into the data warehouse.

### 4️⃣ Data Validation

Run tests to ensure data quality.

### 5️⃣ Orchestration

Automate the pipeline using a shell script.

---

# ▶️ Running the Pipeline

Run the entire pipeline with:

```bash
bash run_all.sh
```

Or run individual steps:

### Extract data

```bash
python src/extract.py
```

### Transform data

```bash
python src/transform.py
```

### Load data

```bash
python src/load_to_snowflake.py
```

---

# 🔐 Environment Variables

Create a `.env` file and configure your credentials:

```
SNOWFLAKE_ACCOUNT=
SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_DATABASE=
SNOWFLAKE_SCHEMA=
SNOWFLAKE_WAREHOUSE=
```

---

# 🧪 Testing

Run database tests with:

```
dbt test
```

---

# 🚀 Future Improvements

Possible improvements for the project:

* Add real-time streaming
* Integrate Airflow for orchestration
* Build dashboards for analytics
* Implement automated monitoring

---

# 📌 Author

Muhammad Saud Khalid
Data Engineering Project
