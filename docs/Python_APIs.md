# Python APIs and Scripts

This document describes public Python functions and operational scripts in this repository.

## Database
- SQLite file: `bin_database.db`
- Table: `bin_data`
  ```sql
  CREATE TABLE IF NOT EXISTS bin_data (
      bin_number INTEGER,
      country TEXT,
      bank_name TEXT,
      card_name TEXT,
      card_type TEXT,
      provider_type TEXT,
      base TEXT,
      time_update TEXT,
      note TEXT
  );
  ```

---

## Module: `query_data.py`

### `query_bin(bin_number=None, country=None, bank_name=None, card_type=None, provider_type=None, time_update=None, note=None) -> list[tuple]`
Executes a parameterized search against `bin_data`. A hard `LIMIT 100` is applied.

- **Parameters** (all optional):
  - `bin_number`: exact match (int or str)
  - `country`: substring match (`LIKE '%value%'`)
  - `bank_name`: substring match
  - `card_type`: exact match
  - `provider_type`: exact match
  - `time_update`: substring match (e.g., `YYYY-MM-DD`)
  - `note`: substring match
- **Returns**: `list[tuple]` of rows in column order shown in the schema.
- **Example**
  ```python
  from query_data import query_bin

  # Sample query
  rows = query_bin(country="UNITED STATES", provider_type="PERSONAL")
  for row in rows:
      print(row)
  ```
- **Behavior notes**:
  - Opens a new SQLite connection per call and closes it.
  - Max 100 rows returned.

---

## Module: `app.py` (server utilities)

### `get_unique_values(column: str) -> list[str]`
Fetches distinct, non-NULL values for a given column from `bin_data`, ordered ascending.

- **Parameters**:
  - `column`: one of `country`, `bank_name`, `card_name`, `card_type`, `provider_type`.
- **Returns**: list of strings.
- **Example**
  ```python
  from app import get_unique_values
  countries = get_unique_values("country")
  ```

### `get_options()` (Flask view)
Returns a JSON payload aggregating distinct values across multiple columns. Exposed as `GET /get_options`.

### `index()` (Flask view)
Renders the search form (`GET /`) and processes form submissions (`POST /`). Applies `LIMIT 100`.

---

## Operational scripts

### `create_database.py`
Creates the `bin_data` table in `bin_database.db` if it doesn’t exist.
```bash
python create_database.py
```
Output: `Đã tạo bảng thành công!`

### `import_data.py`
Imports CSV data into the `bin_data` table, replacing existing data.

- Looks for `bin_data.csv` in the working directory.
- Expects 9 columns; they are mapped to the schema in this order:
  `bin_number, country, bank_name, card_name, card_type, provider_type, base, time_update, note`

```bash
python import_data.py
```
Output: `Đã nhập dữ liệu thành công!`

> Warning: Uses `if_exists="replace"`, which overwrites existing table data.

### `create_indexes.py`
Creates indexes to speed up common queries.
```bash
python create_indexes.py
```
Output: `Đã tạo index thành công!`

### `check_data.py`
Prints the total row count and the first 5 rows for sanity checking.
```bash
python check_data.py
```

---

## Environment & runtime
- Python dependencies: `Flask`, `pandas` (see `requirements.txt`).
- SQLite database file must be present in the working directory.
- The web server binds `0.0.0.0` and reads the port from `PORT` (default 5000).
