# 🛒 E-Commerce Data Engineering Pipeline using Databricks

> **Building scalable ETL pipelines using Databricks, PySpark, Spark SQL, and Delta Lake with the Medallion Architecture to transform raw data into analytics-ready insights.**

---

## 📖 Overview

This repository demonstrates an **End-to-End Data Engineering Pipeline** built using **Databricks Community Edition**, **Apache Spark**, **PySpark**, **Spark SQL**, and **Delta Lake**.

The project follows the **Medallion Architecture (Bronze → Silver → Gold)** to ingest raw e-commerce datasets, perform data cleansing and transformation, and create analytics-ready dimension and fact tables.

The implementation showcases real-world Data Engineering concepts such as schema enforcement, metadata tracking, Delta Lake storage, ETL pipeline development, and data quality validation.

---

## 🚀 Key Features

- End-to-End ETL Pipeline
- Medallion Architecture (Bronze → Silver → Gold)
- Schema Enforcement
- Data Validation
- Metadata Tracking
- Data Cleaning & Standardization
- Delta Lake Storage
- Dimension & Fact Processing
- Analytics-Ready Gold Layer
- Modular Databricks Notebooks

---

## 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Databricks Community Edition | Development Environment |
| Apache Spark | Distributed Data Processing |
| PySpark | Data Transformation |
| Spark SQL | SQL-Based Transformations |
| Delta Lake | Data Storage |
| Unity Catalog | Catalog & Schema Management |
| Git | Version Control |
| GitHub | Source Code Management |

---

# 📂 Repository Structure

```text
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
│   ├── medallion_processing_dim/
│   │   ├── 1_dim_bronze.py
│   │   ├── 2_dim_silver.py
│   │   └── 3_dim_gold.py
│   │
│   └── medallion_processing_fact/
│       ├── 1_fact_bronze.py
│       ├── 2_fact_silver.py
│       └── 3_fact_gold.py
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
└── docs/
    ├── project_overview.md
    ├── execution_guide.md
    └── data_dictionary.md
```

---

# 📊 Dataset

The project processes multiple e-commerce datasets including:

### Dimension Data

- Brands
- Categories
- Products
- Customers
- Calendar (Date)

### Fact Data

- Order Items

---

# 🏗 Medallion Architecture

## 🥉 Bronze Layer

The Bronze layer stores raw data exactly as received from the source system.

### Responsibilities

- Read CSV files
- Apply predefined schemas
- Preserve source data
- Capture metadata
- Store Delta tables

### Bronze Tables

- brz_brands
- brz_category
- brz_products
- brz_customers
- brz_calendar
- brz_order_items

---

## 🥈 Silver Layer

The Silver layer cleans and standardizes the Bronze data.

### Data Quality Operations

- Duplicate Removal
- NULL Handling
- Data Type Conversion
- String Standardization
- Schema Validation
- Business Rule Validation
- Data Cleansing
- Metadata Preservation
- Anomaly Correction

### Silver Tables

- slv_brands
- slv_category
- slv_products
- slv_customers
- slv_calendar
- slv_order_items

---

## 🥇 Gold Layer

The Gold layer prepares curated datasets for analytics and reporting.

### Dimension Tables

- Product Dimension
- Customer Dimension
- Calendar Dimension

### Fact Tables

- Sales Fact
- Order Fact *(if implemented)*

The Gold layer is optimized for downstream analytics, dashboards, and business reporting.

---

# ⚙️ Execution Order

Execute the notebooks in the following sequence.

## Step 1

```
setup/01_ecommerce_setup.py
```

Creates:

- Catalog
- Bronze Schema
- Silver Schema
- Gold Schema

---

## Step 2

Run the Dimension Bronze notebook

```
notebooks/medallion_processing_dim/1_dim_bronze.py
```

This notebook:

- Reads raw dimension datasets
- Applies schemas
- Adds metadata columns
- Loads Bronze Delta Tables

---

## Step 3

Run the Dimension Silver notebook

```
notebooks/medallion_processing_dim/2_dim_silver.py
```

This notebook performs:

- Data Cleaning
- Duplicate Removal
- NULL Handling
- Data Validation
- Standardization
- Data Type Conversion

---

## Step 4

Run the Dimension Gold notebook

```
notebooks/medallion_processing_dim/3_dim_gold.py
```

This notebook creates:

- Product Dimension
- Customer Dimension
- Date Dimension

---

## Step 5

Run Fact Processing

```
notebooks/medallion_processing_fact/
```

Execution order:

```
1_fact_bronze.py

↓

2_fact_silver.py

↓

3_fact_gold.py
```

This pipeline processes transactional data and prepares analytics-ready fact tables.

---

# 📋 Data Quality Checks

The project implements several data quality techniques including:

- Schema Validation
- Duplicate Detection
- Duplicate Removal
- NULL Value Handling
- Metadata Tracking
- Data Standardization
- String Cleaning
- Business Rule Validation
- Data Type Conversion
- Data Quality Monitoring

---

# 💡 Skills Demonstrated

This project demonstrates practical experience with:

- Data Engineering
- ETL Pipeline Development
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- Databricks
- Unity Catalog
- Medallion Architecture
- Data Cleaning
- Data Validation
- Data Transformation
- Data Modeling
- Metadata Management
- Git
- GitHub

---

# 🎯 Business Outcome

This project transforms raw e-commerce data into curated datasets suitable for:

- Business Intelligence
- Reporting
- Dashboard Development
- Customer Analytics
- Product Analytics
- Sales Analytics
- Data Warehousing

---

# 📈 Future Enhancements

Potential improvements include:

- Incremental Data Loading
- Slowly Changing Dimensions (SCD)
- Delta Live Tables (DLT)
- Databricks Workflows
- Automated Testing
- CI/CD Pipeline
- Azure Data Factory Integration
- Power BI Dashboard
- Performance Optimization