# Usage & Examples

This guide walks through environment setup, database preparation, running the Flask server, and querying data via the UI and programmatically.

## 1) Environment Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Dependencies:
- Flask
- pandas (for CSV import script)

## 2) Database Preparation
Create the database schema:
```bash
python create_database.py
```

Place your source data as `bin_data.csv` in the project root, then import:
```bash
python import_data.py
```

Create indexes (optional but recommended):
```bash
python create_indexes.py
```

Quickly verify data presence:
```bash
python check_data.py
```

## 3) Run the Web App
```bash
export PORT=5000  # optional, defaults to 5000
python app.py
# Visit http://localhost:5000
```

## 4) Using the UI
- Browse to `/` to see the search form.
- Dropdowns auto-populate from `/get_options`.
- Submit the form to view results (max 100 rows).

## 5) API Examples

### Get dropdown option values
```bash
curl -s http://localhost:5000/get_options | jq
```

### Post a search (HTML response)
```bash
curl -s -X POST \
  -F "country=UNITED STATES" \
  -F "provider_type=PERSONAL" \
  http://localhost:5000/ > results.html
open results.html  # or xdg-open results.html
```

## 6) Programmatic Queries (Python)
Use `query_data.query_bin` for structured access:
```python
from query_data import query_bin

# By country and provider type
rows = query_bin(country="UNITED STATES", provider_type="PERSONAL")
for row in rows[:3]:
    print(row)

# Exact bin number
rows = query_bin(bin_number=123456)
print(len(rows), "rows")

# Partial matches (LIKE): country, bank_name, time_update, note
rows = query_bin(bank_name="CHASE")
print(rows[:2])
```

Notes:
- The helper connects to `bin_database.db` in the project root.
- A `LIMIT 100` is applied.
