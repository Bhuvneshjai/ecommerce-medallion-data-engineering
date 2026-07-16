# Project Overview

This project implements an end-to-end ETL pipeline using Databricks and the Medallion Architecture.

The objective is to ingest raw e-commerce datasets, improve data quality through cleansing and transformations, and generate analytics-ready dimension tables for downstream reporting.

The project is divided into three processing layers:

- Bronze Layer – Raw data ingestion
- Silver Layer – Data cleansing and standardization
- Gold Layer – Business-ready dimension tables

The implementation combines PySpark and Spark SQL to perform scalable data engineering operations on Delta Lake.