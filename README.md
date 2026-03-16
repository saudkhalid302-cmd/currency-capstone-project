<<<<<<< HEAD
# 🚀 Currency Exchange Data Pipeline

Yeh project ek automated **ETL pipeline** hai jo real-time currency exchange rates fetch karti hai, unhein process karti hai, aur **Snowflake** data warehouse mein load karti hai.

## 🏗 Architecture
* **Ingestion:** API se data lekar AWS S3 mein store karna (Bronze Layer).
* **Transformation:** Python (Pandas) ka istemal karke data ko clean karna (Silver Layer).
* **Loading:** Saaf data ko Snowflake mein load karna.
* **Infrastructure:** **Terraform** (IaC) ke zariye AWS resources manage karna.
* **Orchestration:** **GitHub Actions** aur ek custom Shell script (`run_all.sh`) se workflow automate karna.

## 📂 Project Structure
```text
├── .github/workflows/  # CI/CD pipelines
├── scripts/            # Data fetch karne ki scripts
├── src/                # Transformation & Loading logic
├── terraform/          # Infrastructure-as-Code files
├── run_all.sh          # Orchestration script
└── README.md
=======
Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
>>>>>>> fd711e00b6991d8c07c8896ba470bbfa271be207
