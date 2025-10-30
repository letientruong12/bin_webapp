# Python Modules and Scripts

This project includes a Flask app module and several utility/CLI scripts. Below is a reference of public functions and how to use them.

## `app.py`

### `get_unique_values(column: str) -> list`
Returns a list of distinct, non-NULL values from `bin_data.<column>`, ordered ascending. Used internally by `/get_options`.

Example:
```python
from app import get_unique_values
print(get_unique_values("country")[:10])
```

### Flask routes
- `GET /get_options` — See API doc.
- `GET|POST /` — See API doc.

Environment variables:
- `PORT` — port to bind (default `5000`). The app binds to `0.0.0.0`.

## `query_data.py`

### `query_bin(bin_number=None, country=None, bank_name=None, card_type=None, provider_type=None, time_update=None, note=None) -> list[tuple]`
Executes a parameterized SQL query on `bin_data` with optional filters. Returns up to 100 rows as a list of tuples.

- Exact match: `bin_number`, `card_type`, `provider_type`
- Partial match (LIKE with wildcards added): `country`, `bank_name`, `time_update`, `note`

Example usage:
```python
from query_data import query_bin

# Fetch first 100 US PERSONAL records
rows = query_bin(country="UNITED STATES", provider_type="PERSONAL")
for row in rows[:5]:
    print(row)
```

Notes:
- Uses SQLite file `bin_database.db` in the project root.
- Adds `LIMIT 100` to avoid heavy loads.

## `create_database.py`
Creates the `bin_data` table if it does not exist.

Run:
```bash
python create_database.py
```

Table columns created:
- `bin_number INTEGER`
- `country TEXT`
- `bank_name TEXT`
- `card_name TEXT`
- `card_type TEXT`
- `provider_type TEXT`
- `base TEXT`
- `time_update TEXT`
- `note TEXT`

## `import_data.py`
Imports data from `bin_data.csv` into the `bin_data` table (replaces existing table contents).

Prerequisites:
- `bin_data.csv` present in the project root.
- Columns are standardized internally to: `bin_number,country,bank_name,card_name,card_type,provider_type,base,time_update,note`.

Run:
```bash
python import_data.py
```

## `create_indexes.py`
Creates indexes on frequently queried columns.

Run:
```bash
python create_indexes.py
```

Indexes created:
- `idx_bin_number` on `bin_data(bin_number)`
- `idx_country` on `bin_data(country)`
- `idx_bank_name` on `bin_data(bank_name)`
- `idx_card_type` on `bin_data(card_type)`
- `idx_provider_type` on `bin_data(provider_type)`
- `idx_time_update` on `bin_data(time_update)`

## `check_data.py`
Utility script to quickly inspect row counts and sample rows.

Run:
```bash
python check_data.py
```

Outputs:
- Total rows count
- First 5 rows
