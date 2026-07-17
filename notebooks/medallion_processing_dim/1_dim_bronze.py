# Databricks notebook source
# MAGIC %md
# MAGIC ### Ingest Dimension Data into Bronze Layer

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, TimestampType, FloatType
import pyspark.sql.functions as F

# COMMAND ----------

catalog_name = 'ecommerce'

# COMMAND ----------

# MAGIC %md
# MAGIC ### Brands

# COMMAND ----------

# Define Schema For Data File
brand_schema = StructType([
    StructField("brand_code", StringType(), False),
    StructField("brand_name", StringType(), True),
    StructField("category_code", StringType(), True)
])

# COMMAND ----------

raw_data_path = "/Volumes/ecommerce/source_data/raw_data/brands/*.csv"
df = spark.read.option('header', 'true').option('delimiter',',').schema(brand_schema).csv(raw_data_path)

# Add Metadata Columns
df = df.withColumn("_source_file", F.col("_metadata.file_path")) \
        .withColumn("ingested_at", F.current_timestamp())

display(df.limit(5))

# COMMAND ----------

df.write.format("delta") \
    .mode("overwrite") \
    .option("mergeSchema", "true") \
    .saveAsTable(f"{catalog_name}.bronze.brz_brands")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Category

# COMMAND ----------

category_schema = StructType([
    StructField("category_code", StringType(), False),
    StructField("category_name", StringType(), True)
])

# Load Data Using Schema Defined
raw_data_path = "/Volumes/ecommerce/source_data/raw_data/category/*.csv"

df_category = spark.read.option("header", "true").option("delimeter", ",").schema(category_schema).csv(raw_data_path)

# Add Metadata Colmns
df_category = df_category.withColumn("_ingested_at", F.current_timestamp()) \
                        .withColumn("_source_file", F.col("_metadata.file_path"))

# Write Raw Data into Bronze Layer
df_category.write.format("delta") \
    .mode("overwrite") \
    .option("mergeSchema", "true") \
    .saveAsTable(f"{catalog_name}.bronze.brz_category")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Products

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW VOLUMES IN ecommerce.source_data

# COMMAND ----------

products_schema = StructType([
    StructField("product_id", StringType(), False),
    StructField("sku", StringType(), True),
    StructField("category_code", StringType(), True),
    StructField("brand_code", StringType(), True),
    StructField("color", StringType(), True),
    StructField("size", StringType(), True),
    StructField("material", StringType(), True),
    StructField("weight_grams", StringType(), True),  #datatype is string due to incoming data contain anamolies
    StructField("length_cm", StringType(), True),     #datatype is string due to incoming data contain anamolies
    StructField("width_cm", FloatType(), True),
    StructField("height_cm", FloatType(), True),
    StructField("rating_count", IntegerType(), True),
    StructField("file_name", StringType(), False),
    StructField("ingest_timestamp", TimestampType(), False)
])

# Load Data using the schema defined
raw_data_path = "/Volumes/ecommerce/source_data/raw_data/products/*.csv"

df = spark.read.option("header", "true").option("delimeter", ",").schema(products_schema).csv(raw_data_path) \
        .withColumn("file_name", F.col("_metadata.file_path")) \
            .withColumn("ingest_timstamp", F.current_timestamp())

# Write raw data to Bronze Layer
df.write.format("delta") \
  .mode("overwrite") \
  .option("mergeSchema", "true") \
  .saveAsTable(f"{catalog_name}.bronze.brz_products")

# COMMAND ----------

customers_schema = StructType([
    StructField("customer_id", StringType(), False),
    StructField("phone", StringType(), True),
    StructField("country_code", StringType(), True),
    StructField("country", StringType(), True),
    StructField("state", StringType(), True)
])

# Load data using the schema defined
raw_data_path ="/Volumes/ecommerce/source_data/raw_data/customers/*.csv"

df_raw = spark.read.option("header", "true").option("delimiter", ",").schema(customers_schema).csv(raw_data_path) \
    .withColumn("file_name", F.col("_metadata.file_path")) \
    .withColumn("ingest_timestamp", F.current_timestamp())

# Write raw data to the Bronze layer (catalog: ecommerce, schema: bronze, table: brz_customers)
df_raw.write.format("delta") \
    .mode("overwrite") \
    .option("mergeSchema", "true") \
    .saveAsTable(f"{catalog_name}.bronze.brz_customers")      

# COMMAND ----------

# MAGIC %md
# MAGIC ### Date

# COMMAND ----------


# Define schema for the data file
date_schema = StructType([
    StructField("date", StringType(), True),           # Raw date in string format
    StructField("year", IntegerType(), True),          # Year
    StructField("day_name", StringType(), True),       # Day name (can be mixed case)
    StructField("quarter", IntegerType(), True),       # Quarter
    StructField("week_of_year", IntegerType(), True),  # Week of year (can be negative)
])

# Load data using the schema defined
raw_data_path = f"/Volumes/ecommerce/source_data/raw_data/date/*.csv" 

df_raw = spark.read.option("header", "true").option("delimiter", ",").schema(date_schema).csv(raw_data_path)

# Add metadata columns
df_raw = df_raw.withColumn("_ingested_at", F.current_timestamp()) \
               .withColumn("_source_file", F.col("_metadata.file_path"))


# Write raw data to the Bronze layer (catalog: ecommerce, schema: bronze, table: brz_calendar) 
df_raw.write.format("delta") \
    .mode("overwrite") \
    .option("mergeSchema", "true") \
    .saveAsTable(f"{catalog_name}.bronze.brz_calendar")               