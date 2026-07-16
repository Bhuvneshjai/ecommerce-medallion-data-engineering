# E-Commerce Data Engineering Pipeline using Databricks

## Overview

This project demonstrates an end-to-end Data Engineering pipeline built on **Databricks** using **PySpark**, **Spark SQL**, and **Delta Lake**.

The pipeline follows the **Medallion Architecture** (Bronze → Silver → Gold) to ingest, clean, transform, and prepare e-commerce dimension data for analytics and reporting.

The project showcases real-world ETL development practices including schema enforcement, data quality validation, metadata tracking, transformation pipelines, and Delta table creation.

---

## Tech Stack

- Databricks Community Edition
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- Unity Catalog
- Git
- GitHub

---

## Dataset

The project processes multiple e-commerce dimension datasets:

- Brands
- Categories
- Products
- Customers
- Calendar (Date)

---

## Project Structure

```
ecommerce-medallion-data-engineering/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── setup/
│   └── 01_ecommerce_setup.py
│
├── notebooks/
│   └── medallion_processing/
│       ├── 01_dim_bronze.py
│       ├── 02_dim_silver.py
│       └── 03_dim_gold.py
│
├── data/
│   └── sample_data/
│       ├── brands
│       ├── category
│       ├── customers
│       ├── products
│       ├── order_items
│       └── date
│   
│   
│
└── docs/
    ├── project_overview.md
    ├── execution_guide.md
    └── data_dictionary.md
