# Data Dictionary

## Bronze Layer

| Table | Description |
|--------|-------------|
| brz_brands | Raw brand information |
| brz_category | Raw category information |
| brz_products | Raw product data |
| brz_customers | Raw customer data |
| brz_calendar | Raw calendar data |

---

## Silver Layer

| Table | Description |
|--------|-------------|
| slv_brands | Cleaned brand information |
| slv_category | Deduplicated categories |
| slv_products | Standardized product data |
| slv_customers | Cleaned customer information |
| slv_calendar | Standardized calendar data |

---

## Gold Layer

| Table | Description |
|--------|-------------|
| gld_dim_products | Analytics-ready product dimension |
| gld_dim_customers | Customer dimension with region mapping |
| gld_dim_date | Calendar dimension for reporting |