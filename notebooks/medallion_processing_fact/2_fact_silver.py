# Databricks notebook source
# MAGIC %md
# MAGIC ### Bronze to Silver: Data Cleaning and Transformation

# COMMAND ----------

from pyspark.sql.types import StringType, IntegerType, DateType, BooleanType
import pyspark.sql.functions as F

# COMMAND ----------

catalog_name = "ecommerce"

# COMMAND ----------

df = spark.table(f'{catalog_name}.bronze.brz_order_items')
df.show(5)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# Transformation: Drop Any Duplicates
df = df.dropDuplicates(["order_id", "item_seq"])

# Transformation: Convert 'Two' -> 2 and cast to integer
df = df.withColumn(
    "quantity",
    F.when(F.col("quantity") == "Two", 2).otherwise(F.col("quantity")).cast("int")
)

# Transformation: Remove any '$' or other symbols from unit_price, keep only numeric
df = df.withColumn(
    "unit_price",
    F.regexp_replace("unit_price", "[$]", "").cast("double")
)

# Transformation: Remove '%' from discount_pct and cast to double
df = df.withColumn(
    "discount_pct",
    F.regexp_replace("discount_pct", "%", "").cast("double")
)

# Transformation: Channel Processing
df = df.withColumn(
    "channel",
    F.when(F.col("channel") == "web", "Website")
    .when(F.col("channel") == "app", "Mobile")
    .otherwise(F.col("channel"))
)

# COMMAND ----------

# Transformation: Datatype Conversion
# 1) Convert dt (string -> date)
df = df.withColumn(
    "dt",
    F.to_date("dt", "yyyy-MM-dd")
)

# 2) Convert order_ts (string -> timestamp)
df = df.withColumn(
    "order_ts",
    F.coalesce(
        F.to_timestamp("order_ts", "yyyy-MM-dd HH:mm:ss"),
        F.to_timestamp("order_ts", "yyyy-MM-dd HH:mm")
    )
)

# 3) Convert item_seq (string -> integer)
df = df.withColumn(
    "item_seq",
    F.col("item_seq").cast("int")
)

# 4) Convert tax_amount (string -> double, strip non-numeric characters)
df = df.withColumn(
    "tax_amount",
    F.regexp_replace("tax_amount", r"[^0-9.\-]", "").cast("double")
)

# Transformation: Add processed time
df = df.withColumn(
    "processed_time", F.current_timestamp()
)

# COMMAND ----------

display(df.limit(5))

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# Write raw data to the silver layer
df.write.format("delta") \
    .mode("overwrite") \
    .option("mergeSchema", "true") \
    .saveAsTable(f"{catalog_name}.silver.slv_order_items")