# Execution Guide

Execute notebooks in the following order.

## Step 1

Run

setup/01_ecommerce_setup.py

Purpose

- Create Catalog
- Create Bronze Schema
- Create Silver Schema
- Create Gold Schema

---

## Step 2

Run

notebooks/medallion_processing/01_dim_bronze.py

Purpose

- Read CSV files
- Apply schemas
- Add metadata columns
- Create Bronze Delta Tables

---

## Step 3

Run

notebooks/medallion_processing/02_dim_silver.py

Purpose

- Clean data
- Handle null values
- Remove duplicates
- Standardize values
- Create Silver Delta Tables

---

## Step 4

Run

notebooks/medallion_processing/03_dim_gold.py

Purpose

- Build Product Dimension
- Build Customer Dimension
- Build Date Dimension
- Create Gold Delta Tables