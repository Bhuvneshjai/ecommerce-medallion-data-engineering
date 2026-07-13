# Databricks notebook source
# MAGIC %sql
# MAGIC Create Catalog If Not Exists ecommerce;

# COMMAND ----------

# MAGIC %sql
# MAGIC Use Catalog ecommerce;

# COMMAND ----------

# MAGIC %sql
# MAGIC Create Schema If Not Exists ecommerce.bronze;
# MAGIC Create Schema If Not Exists ecommerce.silver;
# MAGIC Create Schema If Not Exists ecommerce.gold;

# COMMAND ----------

# MAGIC %sql
# MAGIC Show Databases From ecommerce;